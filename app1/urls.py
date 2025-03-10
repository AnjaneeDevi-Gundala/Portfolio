from django.urls import path
from .views import *

app_name='app1'

urlpatterns =[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('project/',project,name='project'),
    path('contact/',contact,name='contact'),


]