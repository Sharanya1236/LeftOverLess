from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from django.db.models import Q
from .models import Profile, Food
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "core/index.html")


# ---------------- REGISTER ----------------
def register_view(request):
    if request.method == "POST":
        print("REGISTER POST HIT")

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        role = request.POST.get("role")

        if not all([username, email, password, role]):
            messages.error(request, "All fields are required")
            return redirect("register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("register")


        # 🔥 USE EMAIL AS USERNAME
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        Profile.objects.create(user=user, role=role)

        print("USER CREATED, REDIRECTING TO LOGIN")
        return redirect("login")

    return render(request, "core/register.html")



# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Invalid credentials")
            return redirect("login")

        user = authenticate(
            request,
            username=user_obj.username,
            password=password
        )

        if user:
            login(request, user)
            role = user.profile.role

            if role == "donor":
                return redirect("donor_dashboard")
            elif role == "receiver":
                return redirect("receiver_dashboard")
            elif role == "volunteer":
                return redirect("employee_dashboard")

        messages.error(request, "Invalid credentials")
        return redirect("login")

    return render(request, "core/login.html")


# ---------------- DONOR DASHBOARD ----------------
@login_required

def donor_dashboard(request):
    foods = Food.objects.filter(donor=request.user)

    total_donations = foods.count()
    active_donations = foods.filter(
        Q(status="available") | Q(status="requested")
    ).count()
    delivered_donations = foods.filter(status="delivered").count()
    expired_donations = foods.filter(status="expired").count()

    context = {
        "total": total_donations,
        "active": active_donations,
        "delivered": delivered_donations,
        "expired": expired_donations,
    }

    return render(request, "core/donar_dashboard.html", context)



# ---------------- ADD FOOD ----------------
@login_required
def add_food(request):
    if request.method == "POST":
        prepared_time = timezone.datetime.fromisoformat(
            request.POST["prepared_time"]
        )
        expiry_time = timezone.datetime.fromisoformat(
            request.POST["expiry_time"]
        )

        if expiry_time <= prepared_time:
            messages.error(
                request,
                "Expiry time must be after prepared time"
            )
            return redirect("add_food")

        Food.objects.create(
            donor=request.user,
            food_name=request.POST["food_name"],
            food_type=request.POST["food_type"],
            quantity=request.POST["quantity"],
            prepared_time=prepared_time,
            expiry_time=expiry_time,
            address=request.POST["address"],
            notes=request.POST.get("notes", ""),
            latitude=request.POST.get("latitude"),
            longitude=request.POST.get("longitude"),

        )

        messages.success(request, "Food posted successfully")
        return redirect("food_success")


    return render(request, "core/add_food.html")

@login_required
def food_success(request):
    return render(request, "core/food_success.html")

# ---------------- MY DONATIONS ----------------

@login_required
def my_donations(request):
    foods = Food.objects.filter(donor=request.user).order_by('-created_at')

    # 🔥 AUTO EXPIRY LOGIC (STEP 4)
    for food in foods:
        if food.status == 'available' and food.expiry_time < timezone.now():
            food.status = 'expired'
            food.save()

    return render(request, 'core/my_donations.html', {
        'foods': foods
    })



@login_required
def cancel_donation(request, food_id):
    food = Food.objects.get(id=food_id, donor=request.user)

    if food.status == "available":
        food.status = "cancelled"
        food.save()
        messages.success(request, "Donation cancelled successfully")

    return redirect("my_donations")

# ---------------- OTHER DASHBOARDS ----------------
@login_required
def receiver_dashboard(request):
    return render(request, "core/receiver_dashboard.html")


@login_required
def employee_dashboard(request):
    return render(request, "core/employee_dashboard.html")
