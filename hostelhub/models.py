
# Create your models here.
from django.db import models


class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    available_beds = models.IntegerField()

    def __str__(self):
        return self.room_number 

class Resident(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    joining_date = models.DateField()
    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name="residents"
    )

    def __str__(self):
        return self.name

class Attendance(models.Model):
    STATUS_CHOICES = [
        ("Present", "Present"),
        ("Absent", "Absent"),
    ]

    resident = models.ForeignKey(
        Resident,
        on_delete=models.CASCADE,
        related_name="attendance"
    )
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    def __str__(self):
        return f"{self.resident.name} - {self.date} - {self.status}"