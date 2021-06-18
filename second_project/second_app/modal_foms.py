from django import forms
from second_app.models import User


#my own custom validation
def check_for_z(value):
	if value[0].lower()!='z':
		raise forms.ValidationError("NAME NEED TO START WITH Z")

class NewUserForm(forms.ModelForm):
 	#name=forms.CharField(validators=[check_for_z])
	class Meta():
		model=User
		fields='__all__'