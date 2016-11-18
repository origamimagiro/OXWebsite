from django.shortcuts import render, HttpResponseRedirect, Http404
from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
import os

def index(request):
	return render(request, 'index.html')

def rush(request):
	return render(request, 'templates/rush/main.html')

def alumni(request):
	print os.getcwd()
	return render(request, 'index_alums.html')

def events(request):
	return render(request, 'templates/other/events.html')

def redirect(request):
	return HttpResponseRedirect('/main/')

def summer(request):
	return render(request, 'templates/other/summer_rooming.html')
        
def login(request):
	args = {}
	args.update(csrf(request))
	if request.method == 'GET':
		return render(request, 'templates/other/login.html', args)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_staff:
				return HttpResponseRedirect('/admin/')
			elif user.is_active:
				user_login(request, user)
				# return a 'success page'
				return HttpResponseRedirect('/brotherhood/edit/')
			else:
				# Return a 'disabled account' error message
				return HttpResponseRedirect('/failed/')
		else:
		    # Return an 'invalid login' error message.
		    return HttpResponseRedirect('/failed/')


def bad_login(request):
	return render(request, 'templates/other/failed_login.html')

def handler404(request):
    return render(request,'templates/other/404.html', status=404)

@login_required(login_url='/login/')
def update_password(request):
	args = {}
	args.update(csrf(request))
	user = request.user
	if request.method == 'POST':
		password = request.POST['password']
		password_confirm = request.POST['password2']
		if password_confirm != password:
			return render(request, 'templates/other/404', args)
		else:
			user.set_password(password)
			user.save()
			return HttpResponseRedirect('/brotherhood/edit')
	else:
		pass
	return render(request, 'templates/other/change_password.html', args)


def history(request):
	return render(request, 'templates/history/history.html')

