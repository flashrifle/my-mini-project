from django.shortcuts import redirect, render
from .models import bbs
from .forms import BoardForm
# Create your views here.


def bbs_list(request):
    bbslist = bbs.objects.all().order_by('-id')
    return render(request, 'bbs_list.html', {"bbslist":bbslist})

def bbs_write(request):
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('bbs:list')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'bbs_write.html', context)

def bbs_detail(request, pk):
    bbsdetail = bbs.objects.get(pk=pk)
    return render(request, 'bbs_detail.html', {'bbsdetail':bbsdetail})