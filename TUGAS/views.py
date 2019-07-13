from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect



from django.contrib import messages
from adminpage.models import TambahPengumuman,Dokumentasi


def index(request):
    datapeng    = TambahPengumuman.objects.all().order_by('-updated')
    datadok     = Dokumentasi.objects.all().order_by('-id')
    context = {
        'Datapeng'  : datapeng,
        'Datadok'   : datadok,
    }
    return render(request,'index.html',context)
