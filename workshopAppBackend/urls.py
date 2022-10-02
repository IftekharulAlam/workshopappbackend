from django.urls import path
from . import views
urlpatterns = [
    path('createWorkshop', views.createWorkshop, name='createWorkshop'),
    path('getworkshopList', views.getworkshopList, name='getworkshopList'),
    path('updateWorkshop', views.updateWorkshop, name='updateWorkshop'),
    path('removeWorkshop', views.removeWorkshop, name='removeWorkshop'),
    path('registerUser', views.registerUser, name='registerUser'),
    path('login', views.login, name='login'),
    path('getProfileInfo', views.getProfileInfo, name='getProfileInfo'),
    path('applyForWorkshop', views.applyForWorkshop, name='applyForWorkshop'),

]
