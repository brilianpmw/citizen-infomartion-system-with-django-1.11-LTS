from django.shortcuts import render
from adminpage.models import Dokumentasi

def index(request):
    data = Dokumentasi.objects.all().order_by('-id')
    context = {
        'data' : data,
    }
    return render(request,'dokumentasi/index.html',context)

def detail(request,slugInput):
    data=Dokumentasi.objects.get(slug=slugInput)
    context = {
        'data' : data,
    }

    return render (request,'dokumentasi/detail.html',context)