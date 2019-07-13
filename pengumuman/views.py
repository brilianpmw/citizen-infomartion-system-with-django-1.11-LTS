from django.shortcuts import render
from adminpage.models import TambahPengumuman

# Create your views here.
def index(request):
    databiasa = TambahPengumuman.objects.filter(kategori='bs').order_by('-dibuat')
    datapenting = TambahPengumuman.objects.filter(kategori='sp').order_by('-dibuat')
    context = {
        'databiasa'     : databiasa,
        'datapenting'   : datapenting,
    }
    return render(request,'pengumuman/index.html',context)

def detailpost(request,slugInput):
    pengumuman = TambahPengumuman.objects.get(slug=slugInput)
    context = {
        'pengumuman' : pengumuman,
    }
    return render (request,'pengumuman/detail.html',context)
