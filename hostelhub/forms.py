from django import forms
from django.contrib.auth.models import User
from .models import Room

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

from .models import Attendance, Resident


class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            "name",
            "email",
            "phone",
            "joining_date",
            "room",
        ]

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = [
            "resident",
            "date",
            "status",
        ]

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "room_number",
            "floor",
            "capacity",
            "available_beds",
        ]

