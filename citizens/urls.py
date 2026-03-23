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
   
     path('citizen/', views.citizen,name='citizen'),
     path('change_password_citizen/', views.change_password_citizen,name='change_password_citizen'),
     path('update_password_citizen/', views.update_password_citizen,name='update_password_citizen'),

     path('profile_citizen/', views.profile_citizen,name='profile_citizen'),
     path('profile_edit_citizen/', views.profile_edit_citizen,name='profile_edit_citizen'),
     path('update_cprofile/', views.update_cprofile,name='update_cprofile'),

     path('crime_citizen/', views.crime_citizen,name='crime_citizen'),
     path('add_crime/', views.add_crime,name='add_crime'),
     path('save_crime/', views.save_crime,name='save_crime'),
     path('crime_citizen/', views.crime_citizen, name='crime_citizen'),
     
     path('edit_reported_crimes/<int:cid>/', views.edit_reported_crimes, name='edit_reported_crimes'),
     path('update_reported_crimes/', views.update_reported_crimes, name='update_reported_crimes'),
     path('delete_reported_crimes/<int:cid>/', views.delete_reported_crimes, name='delete_reported_crimes'),
     path('evidence_citizen/<int:cid>/', views.evidence_citizen, name='evidence_citizen'),
     path('save_evidence', views.save_evidence, name='save_evidence'),
     path('edit_evidence_citizen/<int:eid>/', views.edit_evidence_citizen, name='edit_evidence_citizen'),
     path('update_evidence/', views.update_evidence, name='update_evidence'),
     path('delete_evidence/<int:eid>/', views.delete_evidence, name='delete_evidence'),
     path('citizen_crime_laws/', views.citizen_crime_laws, name='citizen_crime_laws'),
     path('citizen_law_description/', views.citizen_law_description, name='citizen_law_description'),
]
