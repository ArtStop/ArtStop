from django.shortcuts import render, get_object_or_404, redirect

# views here.
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Stop, Comment
from .filters import StopFilter
from django.contrib.gis.geos import Point
from comments.forms import CommentForm
from django.contrib.auth.decorators import user_passes_test
import json, requests
info = requests.get('http://ipinfo.io/json').json()
result = [x.strip() for x in info['loc'].split(',')]
latitude, longitude = result

user_location = Point(float(longitude), float(latitude), srid=4326)

class Home(generic.ListView):
    model = Stop
    context_object_name = 'stops'
    queryset = Stop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')

    template_name = 'stops/index.html'
    """qs_names = [stop.name for stop in Stop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')]
    queryset = Stop.objects.all().filter(name__in=qs_names)"""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StopFilter(self.request.GET, queryset=self.get_queryset())
        return context

class StopDetailView(generic.DetailView):
    model = Stop

def add_comment_to_stop(request, pk):
    stop = get_object_or_404(Stop, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.stop = stop
            comment.save()
            return redirect('stop-detail', pk=comment.stop.pk)
    else:
        form = CommentForm()
    return render(request, 'stops/add_comment_to_stop.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('stop-detail', pk=comment.stop.pk)

@user_passes_test(lambda u: u.is_superuser)
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('stop-detail', pk=comment.stop.pk)
