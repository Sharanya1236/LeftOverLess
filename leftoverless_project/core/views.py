from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def donor_login(request):
    return render(request, 'core/donor_login.html')
def donor_dashboard(request):
    return render(request, 'core/donor_dashboard.html')
def post_food(request):
    return render(request, 'core/post_food.html')
def service_login(request):
    return render(request, 'core/service_login.html')

def service_dashboard(request):
    return render(request, 'core/service_dashboard.html')
