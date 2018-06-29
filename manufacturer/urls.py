from django.urls import path, include
from . import views


app_name = "manufacturer"
urlpatterns = [
    path("dashboard", views.index, name="home"),
    path("generate_id", views.GenerateIdView.as_view(), name="generate_id"),

]