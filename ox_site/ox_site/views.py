from django.shortcuts import render, render_to_response, RequestContext
from people.models import Brother
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	args = {'test': 'context works'}
	return render_to_response('index.html', args, context_instance=RequestContext(request))

def brotherhood(request):
	henry = Brother.objects.all()
	args = {'bros':henry}
	print(args)
	return render_to_response('brotherhood.html', args, context_instance=RequestContext(request))

def rush(request):
	return render_to_response('rush.html', context_instance=RequestContext(request))

def events(request):
	return render_to_response('events.html', context_instance=RequestContext(request))