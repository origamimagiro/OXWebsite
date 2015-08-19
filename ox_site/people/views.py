from django.shortcuts import render, HttpResponse, Http404
from people.models import Brother
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
	return HttpResponse('VALID')

def bro_info(request, args):
	try:
		user = User.objects.get(username=args)
		brother = Brother.objects.get(user=user)
		return HttpResponse(str(brother))
	except ObjectDoesNotExist:
		raise Http404('ERROR')

