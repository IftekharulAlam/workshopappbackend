from django.urls import path
from . import views
urlpatterns = [
    path('createWorkshop', views.createWorkshop, name='createWorkshop'),
    path('getworkshopList', views.getworkshopList, name='getworkshopList'),
    
]