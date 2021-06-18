from django.conf.urls import url
from second_app import views

# TEMPLATING TAGGING
app_name='second_app'

urlpatterns=[
url(r'^$',views.users,name="users"),
url(r'^$',views.help,name="help"),
url(r'^relative/$',views.relative,name='relative'),
url(r'^other/$',views.other,name="other"),
]