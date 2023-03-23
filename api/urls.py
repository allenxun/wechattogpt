from django.urls import path
from api import views

urlpatterns = [
    path(r"", views.index, name="home"),
]
