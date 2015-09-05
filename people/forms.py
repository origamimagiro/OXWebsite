from django import forms
from people.models import Brother

class UploadImageForm(forms.Form):
    image = forms.ImageField()


class UpdateBrotherForm(forms.ModelForm):
	class Meta:
		model = Brother
		fields = ['image', 'class_year', 'major', 'hometown', 'about', 'campus_involvement']
		widgets = { 
            'about': forms.Textarea(),
            'campus_involvement': forms.Textarea(),
        }  