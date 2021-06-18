from django import forms
from django.core import validators

#my own validator
#my own custom validation
def check_for_z(value):
	if value[0].lower()!='z':
		raise forms.ValidationError("NAME NEED TO START WITH Z")


class FormName(forms.Form):
	# name=forms.CharField(validators=[check_for_z])
	name=forms.CharField()
	email=forms.EmailField()
	text=forms.CharField(widget=forms.Textarea)
	verify_email=forms.EmailField(label='Verify Email')
	botcatcher=forms.CharField(required=False,
								widget=forms.HiddenInput,
								validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_cleaned_data=super().clean()
		email=all_cleaned_data["email"]
		vmail=all_cleaned_data["verify_email"]

		if email!=vmail:
			raise forms.ValidationError('Email doesn\'t match')




	# def clean_botcatcher(self):
	# 	botcatcher=self.cleaned_data['botcatcher']

	# 	if len(botcatcher)>0:
	# 		raise forms.ValidationError('GOTCHA BOT')
	# 	return botcatcher	