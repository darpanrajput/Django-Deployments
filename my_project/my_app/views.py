from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import AccessRecord,Topic,Webpage

# Create your views here.


def index(request):
	webpages_list=AccessRecord.objects.order_by('date')
	date_dict={'access_record':webpages_list}
	# my_dict={"insert_me":"hello i am from views.py !"}
	return render(request,"my_app/index.html",context=date_dict)

