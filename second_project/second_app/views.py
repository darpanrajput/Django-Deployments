from django.shortcuts import render
from django.conf.urls import url
from django.http import HttpResponse
from second_app.models import User
from second_app import forms
from second_app.modal_foms import NewUserForm

# Create your views here.

def index(request):
	context_dict={'text':'hello world','number':100}
	
	# return HttpResponse("Hello!")
	return render(request,'second_app/index.html',context=context_dict)


def second_app(request):
	helpdict={'help_insert':'HELP PAGE'}
	return render(request,'second_app/index.html',context=helpdict)

def help(request):
	helpdict={'help_insert':'HELP PAGE'}
	return render(request,'second_app/help.html',context=helpdict)


def users(request):
	user_list=User.objects.order_by('first_name')
	user_dict={'users':user_list}
	return render(request,'second_app/users.html',context=user_dict)	


def form_name_view(request):
	form=forms.FormName()

	if request.method=='POST':
		form =forms.FormName(request.POST)

		if form.is_valid():
			# do something
			print("VALIDATION DONE")
			print("NAME "+form.cleaned_data['name'])
			print("EMAIL "+form.cleaned_data['email'])
			print("TEXT "+form.cleaned_data['text'])

	return render(request,'second_app/form_page.html',{'form':form})


def modalform(request):
	form =NewUserForm()


	if request.method=='POST':
		form=NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print("ERROR")	



	# return render(request,'second_app/form_modal.html',context={"key":1})
	return render(request,'second_app/form_modal.html',{"form":form})


def relative(request):
	return render(request,'second_app/relative_url_templates.html')

def other(request):
	return render(request,'second_app/other.html')