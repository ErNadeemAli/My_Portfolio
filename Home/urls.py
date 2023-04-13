from django.urls import path
from .views import *

urlpatterns = [
    path('',homepage,name='home'),
    path('projects',project,name='project'),
    path('Calculator',cal,name='cal'),

]
