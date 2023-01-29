from django.urls import path
from . import views
urlpatterns = [
    path("",views.Home,name='Home'),
    path("room/<int:pk>/",views.room,name='Room'),
    path("createroom/",views.forms,name="Create"),
    path("updateroom/<int:pk>/",views.updateRoom,name="updateRoom"),
    path("deleteroom/<int:pk>/",views.deleteRoom,name="DeleteRoom")
]