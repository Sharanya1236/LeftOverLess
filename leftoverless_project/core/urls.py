from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),

    path("donor/dashboard/", views.donor_dashboard, name="donor_dashboard"),
    path("receiver/dashboard/", views.receiver_dashboard, name="receiver_dashboard"),
    path("employee/dashboard/", views.employee_dashboard, name="employee_dashboard"),
    path("donor/add-food/", views.add_food, name="add_food"),
    path("donor/my-donations/", views.my_donations, name="my_donations"),
    path("donor/food-success/", views.food_success, name="food_success"),
    path("donor/cancel/<int:food_id>/", views.cancel_donation, name="cancel_donation"),
    path("receiver/available-food/", views.available_food, name="available_food"),
    path("logout/", views.logout_view, name="logout"),
    path("receiver/available-food/", views.available_food, name="available_food"),
    path('receiver/request/<int:food_id>/', views.request_food, name='request_food'),
    path('donor/approve/<int:food_id>/', views.approve_request, name='approve_request'),
    path('donor/reject/<int:food_id>/', views.reject_request, name='reject_request'),
    path('donor/requests/', views.donor_requests, name='donor_requests'),
    path('donor/requests/approve/<int:food_id>/', views.approve_request, name='approve_request'),
    path('donor/requests/reject/<int:food_id>/', views.reject_request, name='reject_request'),
    path('receiver/my-requests/', views.my_requests, name='my_requests'),
    path('donor/incoming-requests/', views.donor_incoming_requests, name='donor_incoming_requests'),
    path('employee/dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/requests/', views.employee_requests, name='employee_requests'),
    path('employee/active/', views.employee_active, name='employee_active'),
    path('employee/history/', views.employee_history, name='employee_history'),
    path('employee/accept/<int:food_id>/', views.employee_accept_delivery, name='employee_accept_delivery'),
    path('employee/delivered/<int:food_id>/', views.employee_mark_delivered, name='employee_mark_delivered'),
    path('employee/accept/<int:food_id>/', views.employee_accept_delivery, name='employee_accept_delivery'),
    path('employee/active/', views.employee_active, name='employee_active'),
    path('employee/picked/<int:food_id>/', views.employee_mark_picked, name='employee_mark_picked'),
    path('employee/delivered/<int:food_id>/', views.employee_mark_delivered, name='employee_mark_delivered'),
    path('employee/history/', views.employee_history, name='employee_history'),
    path('logout/', views.logout_view, name='logout'),

]
