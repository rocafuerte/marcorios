from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
#from django.core.urlresolvers import reverse
from django.template import RequestContext
from marcorios.homepage.models import ShowStyle, TextImage, OnlyText, Place


# Determine which template to use
# Want to know which showStyle the id should be regarded as
def show_style(request,showstyle_id):
    # Dis is ugly!
    try:
        style = TextImage.objects.get(pk=showstyle_id)
    except Exception as e:
        pass
    try:
        style = OnlyText.objects.get(pk=showstyle_id)
    except Exception as e:
        pass
    #raise Http404
    
    top = ShowStyle.objects.filter(visible_places=Place.objects.filter(name='Top'))
    return render_to_response('marcorios/image_show.html', {
            'object': style,
            'top': top ,
            'error_message': "You didn't select a choice.",
            }, context_instance=RequestContext(request))
