from django.shortcuts import render
from .models import bbs
# Create your views here.


def bbs_list(request):
    bbslist = bbs.objects.all().order_by('-id')
    return render(request, 'bbslist.html', {"bbslist":bbslist})