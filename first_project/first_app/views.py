from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


# def index(request):
# 	print(HttpResponse("Hello world"))
# 	return HttpResponse("Hello world")


def index(request):
	my_dict={"insert_me":"hello i am from views.py !"}
	return render(request,"first_app/index.html",context=my_dict)

