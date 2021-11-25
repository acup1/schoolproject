from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage,name="main"),
    path('pr', views.pr,name="pr"),
]
