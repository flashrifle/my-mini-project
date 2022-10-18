from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증 성공")
        else:
            print("인증 실패")
    return render(request, "users/login.html")
