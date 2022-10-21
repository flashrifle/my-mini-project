from django.urls import path
from bbs import views

app_name = "bbs"

urlpatterns = [
    path("list/", views.bbs_list, name="list"),
    path("write/", views.bbs_write, name="write")
]