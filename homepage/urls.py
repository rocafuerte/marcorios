from django.conf.urls.defaults import *
from marcorios.homepage.models import *

info_dict = {
    'queryset': ShowStyle.objects.all(), # Wrong. should list all shoestyles here
}

urlpatterns = patterns('',
      (r'(?P<showstyle_id>\d+)$', 'marcorios.homepage.views.show_style'),
)
