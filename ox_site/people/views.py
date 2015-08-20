from django.shortcuts import render, HttpResponse, Http404
from people.models import Brother
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
	return HttpResponse('VALID')

def brother_profile(request, args):
	try:
		user = User.objects.get(username=args)
		brother = Brother.objects.get(user=user)
		args = {'brother':brother}
		return render(request, 'templates/brotherhood/spotlight.html', args)
	except ObjectDoesNotExist:
		raise Http404('ERROR')

