from django.urls import path
from . import views
urlpatterns = [
    path('createWorkshop', views.createWorkshop, name='createWorkshop'),
    path('getworkshopList', views.getworkshopList, name='getworkshopList'),
    path('updateWorkshop', views.updateWorkshop, name='updateWorkshop'),
    path('removeWorkshop', views.removeWorkshop, name='removeWorkshop'),
    
]