from django.shortcuts import render, HttpResponse, Http404
from people.models import Brother
from django.contrib.auth.admin import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

def brother_profile(request, args):
	try:
		user = User.objects.get(username=args)
		brother = Brother.objects.get(user=user)
		args = {'brother':brother}
		return render(request, 'templates/brotherhood/spotlight.html', args)
	except ObjectDoesNotExist:
		raise Http404('ERROR')


def all_brothers(request):
	all_bros = Brother.objects.all()
	args = {'brothers':all_bros}
	return render(request, 'templates/brotherhood/everyone.html', args)

@login_required
def update_profile(request):
	user = request.user
	brother = Brother.objects.get(user=user)
	args = {'brother':brother}
	if request.method == 'POST':
		brother.major = request.POST['major']
		brother.campus_involvement = request.POST['campus_involvement']
		brother.about = request.POST['about']
		brother.hometown = request.POST['hometown']
		brother.save()
	return render(request, 'templates/other/edit_profile.html', args)
