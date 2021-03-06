import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_project.settings')

import django
django.setup()

from my_app.models import AccessRecord,Topic,Webpage

from faker import Faker

import random
fakegen=Faker()
topics=['Search','Social','Market_place','News'
,'Games']


def add_topic():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def popuplate(N=5):
	for entry in range(N):
		top=add_topic()
		fake_url=fakegen.url()	
		fake_date=fakegen.date()	
		fake_name=fakegen.company()	

		webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]


		acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]


if __name__ == '__main__':
	print("popuplating....")
	popuplate(20)
	print("popuplating completed")		
