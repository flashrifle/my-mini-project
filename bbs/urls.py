from django.urls import path
from bbs import views

app_name = "bbs"

urlpatterns = [
    path("bbslist/", views.bbs_list, name="bbslist")
]