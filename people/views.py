from django.shortcuts import render, HttpResponse, Http404, HttpResponseRedirect
from people.models import Brother
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from people.forms import UploadImageForm, UpdateBrotherForm
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
	all_bros = Brother.objects.all().order_by('class_year')
	args = {'brothers':all_bros}
	return render(request, 'templates/brotherhood/everyone.html', args)

@login_required(login_url='/login/')
def update_profile(request):
	user = request.user
	brother = Brother.objects.get(user=user)
	form = UpdateBrotherForm(instance=brother)
	if request.method == 'POST':
		form = UpdateBrotherForm(request.POST, request.FILES, instance=brother)
		if form.is_valid():
			print(request.FILES)
			print(form)
			form.save()		
	args = {'brother': brother, 'form':form}
    args.update(csrf(request))
	return render(request, 'templates/other/edit_profile.html', args)



