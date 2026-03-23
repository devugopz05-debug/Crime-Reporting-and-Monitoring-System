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
   
    path('inv_dashboard/', views.inv_dashboard,name='inv_dashboard'),
    path('change_password_inv/', views.change_password_inv,name='change_password_inv'),
    path('update_password_inv/', views.update_password_inv,name='update_password_inv'),

    path('profile_invesigator/', views.profile_invesigator,name='profile_invesigator'),
    path('profile_edit_nvesigator/', views.profile_edit_nvesigator,name='profile_edit_nvesigator'),
    path('update_inv_profile/', views.update_inv_profile,name='update_inv_profile'),

    path('crime_assigned/', views.crime_assigned,name='crime_assigned'),
    path('crime_location_view/<int:cid>/', views.crime_location_view,name='crime_location_view'),
    path('crime_evidence_inv/<int:cid>/', views.crime_evidence_inv,name='crime_evidence_inv'),
    path('save_evidence_investigator/', views.save_evidence_investigator,name='save_evidence_investigator'),
    path('edit_evidence/<int:edid>', views.edit_evidence,name='edit_evidence'),
    path('update_evidence_details/', views.update_evidence_details,name='update_evidence_details'),
     path('update_evidence/', views.update_evidence,name='update_evidence'),
     path('delete_evidence/<int:eid>', views.delete_evidence,name='delete_evidence'),

     path('investigation_note/<int:cid>/', views.investigation_note,name='investigation_note'),
     path('investigation_note_save/', views.investigation_note_save,name='investigation_note_save'),

     path('edit_investigation_note/<int:nid>', views.edit_investigation_note,name='edit_investigation_note'),
     path('update_note/', views.update_note,name='update_note'),
     path('delete_investigation_note/<int:nid>', views.delete_investigation_note,name='delete_investigation_note'),

     # Reports
     path('inv_reports/monthly/', views.inv_monthly_reports, name='inv_monthly_reports'),
     path('inv_reports/category/', views.inv_category_stats_report, name='inv_category_stats'),
     path('investigation_note/<int:cid>/', views.investigation_note,name='investigation_note'),
     path('save_investigation_note/', views.save_investigation_note,name='save_investigation_note'),
     path('edit_investigation_note/<int:nid>/', views.edit_investigation_note,name='edit_investigation_note'),
     path('update_investigation_note/', views.update_investigation_note,name='update_investigation_note'),
     path('delete_investigation_note/<int:nid>/<int:cid>/', views.delete_investigation_note,name='delete_investigation_note'),
     path('inv_crime_laws/', views.inv_crime_laws,name='inv_crime_laws'),
]
