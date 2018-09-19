import django_filters

from driveso.models import driving

class DrivingFilter(django_filters.FilterSet):
    class Meta:
        model = driving
        fields = {'city': ['icontains'],
		          'area': ['exact'],
                  
                 }    
