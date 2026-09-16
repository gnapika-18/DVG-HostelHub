from django.contrib import admin

# Register your models here.
from .models import Attendance, Room, Resident


admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Attendance)
