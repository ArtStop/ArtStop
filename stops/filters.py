import django_filters
from .models import Stop

class StopFilter(django_filters.FilterSet):

    class Meta:
        model = Stop
        fields =  {'category': ['icontains'],
                    'name': ['icontains']}#('category', 'name')
    
    """@property
    def qs(self):
        parent = super().qs
        #author = getattr(self.request, 'user', None)

        return parent.filter(is_published=True)"""
