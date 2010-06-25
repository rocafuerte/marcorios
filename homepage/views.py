#from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
#from django.core.urlresolvers import reverse
#from django.template import RequestContext
#from marcorios.homepage.models import ShowStyle


# Determine which template to use
def show_style(request,showstyle_id):
    return HttpResponse("Hello, world.")
#s = get_object_or_404(ShowStyle, pk=id)
    #return render_to_response('marcorios/image_show.html', {
    #        'object': p,
    #        'error_message': "You didn't select a choice.",
    #        }, context_instance=RequestContext(request))
