from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from people.models import Brother
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from people.forms import UploadImageForm
from ox_site import settings

def brother_profile(request, args):
	try:
		user = User.objects.get(username=args)
		brother = Brother.objects.get(user=user)
		args = {'brother':brother}
		return render(request, 'templates/brotherhood/spotlight.html', args)
	except ObjectDoesNotExist:
		raise Http404


def all_brothers(request):
	all_bros = Brother.objects.all()
	args = {'brothers':all_bros}
	return render(request, 'templates/brotherhood/everyone.html', args)

@login_required(login_url='/login/')
def update_profile(request):
	user = request.user
	brother = Brother.objects.get(user=user)
	if request.method == 'POST':
		print(request.POST)
		print(request.FILES)
		print(request)
		if 'image' in request.FILES.keys():
			form = UploadImageForm(request.POST, request.FILES)
			print('IMAGE')
			print(form)
			print(form.is_valid())
			if form.is_valid():
				# with open('images/'+user.username+'.jpg', 'wb+') as destination:
				# 	for chunk in request.FILES['image'].chunks():
				# 		# destination.write(chunk)
				# 		print('writing')
				brother.image = request.FILES['image']
				brother.save()
		elif 'password' in request.POST.keys():
			print('PASSWORD')
			password = request.POST['password']
			password_confirm = request.POST['password2']
			user = User.objects.get(username=brother.user.username)
			if password != password_confirm:
				return HttpResponseRedirect('/failed/')
			else:
				user.set_password(password)
				user.save()
				print('SAVED PASSWORD')
				return HttpResponseRedirect('/login/')
		else:
			print('DETAILS')
			brother.major = request.POST['major']
			brother.campus_involvement = request.POST['campus_involvement']
			brother.about = request.POST['about']
			brother.hometown = request.POST['hometown']
			brother.save()
			form = UploadImageForm()
	else:
		form = UploadImageForm()
	args = {'brother':brother, 'form':form}
	return render(request, 'templates/other/edit_profile.html', args)


