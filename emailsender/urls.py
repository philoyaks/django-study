from django.contrib import admin
from django.urls import path
from emailsender import views

urlpatterns = [
    path('', views.createEmailModel, name ='index'),
    path('index', views.createEmailModel, name ='index'),
    path('EditEmailModel/<int:id>', views.editEmailModel, name ='EditEmailModel'),
    path('DeleteEmailModel/<int:id>', views.deleteEmailModel, name ='DeleteEmailModel'),
    path('EditEmailModel/UpdateEmailmodel/<int:id>', views.UpdateEmailModel, name ='UpdateEmailModel'),
    path('sendEmail', views.sendEmail, name ='sendEmail'),


]