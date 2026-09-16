from django.urls import path
from .views import Register, ResidentDeleteView, ResidentUpdateView, add_resident, add_room, attendance_list, dashboard, mark_attendance, resident_list, room_list, user_login, user_logout

urlpatterns = [
    path("", Register, name="home"),
    path('register/', Register, name='register'),
    path('login/', user_login, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path("residents/", resident_list, name="resident_list"),
    path("residents/add/", add_resident, name="add_resident"),
    path("residents/<int:pk>/edit/", ResidentUpdateView.as_view(),name="resident_update"),
    path("residents/<int:pk>/delete/", ResidentDeleteView.as_view(), name="resident_delete"),
    path("attendance/mark/",mark_attendance,name="mark_attendance"),
    path("attendance/list/", attendance_list, name="attendance_list"),
    path("rooms/add/",add_room,name="add_room"),
    path("rooms/",room_list,name="room_list"),
    path("logout/",user_logout,name="logout"),
]