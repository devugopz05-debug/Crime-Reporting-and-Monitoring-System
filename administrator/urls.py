"""
URL configuration for crime_reporting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   
     path('admin/', views.admin,name='admin'),
      path('change_password/', views.change_password,name='change_password'),
      path('update_password/', views.update_password,name='update_password'),
      
       path('category/', views.category,name='category'),
       path('category_save/', views.category_save,name='category_save'),
       path('delete_category/<int:cid>/', views.delete_category,name='delete_category'),
       path('edit_category/<int:cid>/', views.edit_category,name='edit_category'),
       path('update_category/', views.update_category,name='update_category'),

       path('investigator/', views.investigator,name='investigator'),
       path('new_investigator/', views.new_investigator,name='new_investigator'),
       path('investigator_save/', views.investigator_save,name='investigator_save'),
       path('edit_investigator/<int:iid>/', views.edit_investigator,name='edit_investigator'),
       path('update_investigator/', views.update_investigator,name='update_investigator'),
       path('delete_investigator/<int:iid>/', views.delete_investigator,name='delete_investigator'),

       path('citizens/', views.citizens,name='citizens'),

       path('reported_crimes/', views.reported_crimes,name='reported_crimes'),
       path('crime_location/<int:cid>/', views.crime_location,name='crime_location'),

       path('schedule_investigator/<int:cid>/', views.schedule_investigator,name='schedule_investigator'),
       path('assign_investigator/', views.assign_investigator, name='assign_investigator'),
       path('investigation_note/', views.investigation_note, name='investigation_note'),      
       path('inv_note/<int:cid>/', views.inv_note, name='inv_note'),
       path('crime_law/', views.crime_law,name='crime_law'),
       path('crime_law_save/', views.crime_law_save,name='crime_law_save'),            
       path('edit_crime_law/<int:id>/', views.edit_crime_law,name='edit_crime_law'),
       path('update_crime_law/', views.update_crime_law,name='update_crime_law'),
       path('delete_crime_law/<int:id>/', views.delete_crime_law,name='delete_crime_law'),         
]
