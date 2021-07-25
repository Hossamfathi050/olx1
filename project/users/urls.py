 url app 
from django.urls import path
from . import views
from .views import Sc_detailsList

from django.conf.urls import url


app_name = 'sc_details'

urlpatterns = [
    path('' , views.Sc_detailsList.as_view(),name='sc_details_list'),

    path('insert' , views.Sc_details_add,name='insert'),

 

]
