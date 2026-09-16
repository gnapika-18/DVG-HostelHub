from datetime import date
from re import search
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import RegistrationForm,ResidentForm,AttendanceForm, RoomForm
from django.contrib.auth.decorators import login_required
from .models import Attendance, Resident, Room
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import logout



def Register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()

            return redirect("login")

    else:
        form = RegistrationForm()

    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(
            request,
            "login.html",
            {"error": "Invalid username or password."}
        )

    return render(request, "login.html")

@login_required
def dashboard(request):

    total_rooms = Room.objects.count()
    total_residents = Resident.objects.count()

    today = date.today()

    present_today = Attendance.objects.filter(
        date=today,
        status="Present"
    ).count()

    absent_today = Attendance.objects.filter(
        date=today,
        status="Absent"
    ).count()

    return render(
        request,
        "dashboard.html",
        {
            "total_rooms": total_rooms,
            "total_residents": total_residents,
            "present_today": present_today,
            "absent_today": absent_today,
        }
    )


@login_required
def add_resident(request):
    if request.method == "POST":
        form = ResidentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("resident_list")

    else:
        form = ResidentForm()

    return render(request, "add_resident.html", {"form": form})

@login_required
def resident_list(request):
    residents = Resident.objects.all()
    search = request.GET.get("search",'')
    if search:
        residents = residents.filter(
            name__icontains=search
        ) | residents.filter(
            email__icontains=search
        ) | residents.filter(
            phone__icontains=search
        )

    return render(
        request,
        "resident_list.html",
        {
            "residents": residents,
            "search": search
        }
    )
    

class ResidentUpdateView(UpdateView):
    model = Resident
    form_class = ResidentForm
    template_name = "resident_update.html"
    success_url = reverse_lazy("resident_list")

class ResidentDeleteView(DeleteView):
    model = Resident
    template_name = "resident_confirm_delete.html"
    success_url = reverse_lazy("resident_list")

@login_required
def mark_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("attendance_list")

    else:
        form = AttendanceForm()

    return render(
        request,
        "mark_attendance.html",
        {"form": form}
    )

@login_required
def attendance_list(request):
    attendances = Attendance.objects.all().order_by("-date")

    return render(
        request,
        "attendance_list.html",
        {"attendances": attendances}
    )

@login_required
def add_room(request):
    if request.method == "POST":
        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("room_list")

    else:
        form = RoomForm()

    return render(
        request,
        "add_room.html",
        {"form": form}
    )

@login_required
def room_list(request):
    rooms = Room.objects.all()

    return render(
        request,
        "room_list.html",
        {"rooms": rooms}
    )

@login_required
def user_logout(request):
    logout(request)
    return redirect("login")