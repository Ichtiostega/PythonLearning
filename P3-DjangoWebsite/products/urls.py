from django.urls import path
from . import views             #from . because views is a generic name and the products can have other dependencies with a module of the same name. 
                                #That way it is this one.


urlpatterns = [
    path('', views.index),
    path('new', views.new)
]