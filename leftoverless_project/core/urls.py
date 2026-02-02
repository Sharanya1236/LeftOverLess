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


]
