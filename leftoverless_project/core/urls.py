from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #donar
    path('donor/login/', views.donor_login, name='donor_login'),
    path('donor/dashboard/', views.donor_dashboard, name='donor_dashboard'),
    path('donor/post-food/', views.post_food, name='post_food'),
    #service
    path('service/login/', views.service_login, name='service_login'),
    path('service/dashboard/', views.service_dashboard, name='service_dashboard'),


]
