from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='dashboard-index'),
    path('deaths/', views.deaths, name='dashboard-deaths'),
    path('births/', views.births, name='dashboard-births'),
    path('educations/', views.educations, name='dashboard-educations'),

    path('deaths/delete/<int:pk>/', views.death_delete,
         name='dashboard-deaths-delete'),
    path('births/delete/<int:pk>/', views.birth_delete,
         name='dashboard-births-delete'),
    path('educations/delete/<int:pk>/', views.education_delete,
         name='dashboard-educations-delete'),
    
    path('deaths/detail/<int:pk>/', views.death_detail,
         name='dashboard-deaths-detail'),
    path('births/detail/<int:pk>/', views.birth_detail,
         name='dashboard-births-detail'),
     path('educations/detail/<int:pk>/', views.education_detail,
           name='dashboard-educations-detail'),
    
    
    path('deaths/edit/<int:pk>/', views.death_edit,
         name='dashboard-deaths-edit'),
    path('births/edit/<int:pk>/', views.birth_edit,
         name='dashboard-birth-edit'),
     path('educations/edit/<int:pk>/', views.education_edit,
          name='dashboard-educations-edit'),
    
    
    path('customers/', views.customers, name='dashboard-customers'),
    path('customers/detial/<int:pk>/', views.customer_detail,
         name='dashboard-customer-detail'),
]
