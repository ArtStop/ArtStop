import django_filters
from .models import Stop

class StopFilter(django_filters.FilterSet):

    CHOICES = (
            ('museum', 'Museum'),
            ('theatre', 'Theatre'),
            ('church', 'Church')
        )
    category = django_filters.ChoiceFilter(label='Category', choices=CHOICES, method='filter_for_category')
    
    class Meta:
        model = Stop
        
        fields =  {#'category': ['icontains'],
                    'name': ['icontains']}#('category', 'name')

    def filter_for_category(self, queryset, category, value):
        return queryset.filter(category__icontains=value)
