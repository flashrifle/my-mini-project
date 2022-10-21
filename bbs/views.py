from django.shortcuts import render

# Create your views here.


def bbs_list(request):
    return render(request, 'bbslist.html')