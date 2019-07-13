from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from .forms import TambahDokumentasi
from .utlis import render_to_pdf
from django.template.loader import get_template
from django.http import HttpResponse







from django.contrib import messages
from .models import Tambah,TambahPengumuman,Dokumentasi



def index(request):
       
        
        context = { 
                'judul' : 'Halaman admin'
        }
        
        if request.method == "GET":
                if request.user.is_authenticated():   
                        tot_penduduk = Tambah.objects.all().count()
                        tot_pendudukpria = Tambah.objects.filter(jeniskelamin='Pria').count()
                        tot_pendudukwanita = Tambah.objects.filter(jeniskelamin='Wanita').count()
                        
                        
                        context = {
                                'total_penduduk' : tot_penduduk,
                                'pria'           : tot_pendudukpria,
                                'wanita'         : tot_pendudukwanita,
                        }

                        return render(request,'adminpage/index.html',context)
                else:
                        
                        return redirect('masuk')

        if request.method == "POST":
                if request.POST["logout"] == "Submit":
                        logout(request)
                        messages.error(request,'Logout Berhasil, sampai Jumpa!')

                        return redirect('masuk')
               


def masuk(request):
        context = {
            'judul' : 'Login admin',
              
         }
       
        user = None
        if request.method == "POST":
                username_input = request.POST['Username']
                password_input = request.POST['Password']

                user = authenticate(request,username=username_input,password=password_input)

                

                if user == None:
                        messages.error(request,'username atau password salah, jika lupa harap hubungi admin')
                        return redirect('masuk')
                else:
                        login(request,user)
                        return redirect('index')
      


        return render (request,'adminpage/login.html',context)


@login_required(login_url='masuk')
def atur(request):
        if 'tambah' in request.POST:
                if request.POST["tambah"] == "Submit":
                        Tambah.objects.create(
        			nik 		= request.POST.get('nik',False),
        			nama		= request.POST.get('nama',False),
        			tanggallahir	= request.POST.get('tanggallahir',False),
                                jeniskelamin    = request.POST.get('jeniskelamin',False),
                                rt              = request.POST.get('rt',False),
                                alamat          = request.POST.get('alamat',False),
                                updated         = request.POST.get('update',False),
                        )
                        return redirect('atur')
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')


        dataatur= Tambah.objects.all().order_by('-id')
        context= {
                'datauser' : dataatur,
        }

        return render(request,'adminpage/atur.html',context)


@login_required(login_url='masuk')
def delete(request,id_user):
        hapus =  Tambah.objects.get(id=id_user)
        hapus.delete()
     
        return redirect('atur')

@login_required(login_url='masuk')
def update(request,id_user):
        update_id =  Tambah.objects.get(id=id_user)
        context = {
                'nama'          : update_id.nama,
                'nik'           : update_id.nik,
                'jeniskelamin'  : update_id.jeniskelamin,
                'rt'            : update_id.rt,
                'tanggallahir'  : update_id.tanggallahir,
                'alamat'        : update_id.alamat,
        }

        if 'perbarui' in request.POST:
                if request.POST["perbarui"] == "Submit":
                        Tambah.objects.filter(id=id_user).update(
        			nik 		= request.POST.get('nik',False),
        			nama		= request.POST.get('nama',False),
        			tanggallahir	= request.POST.get('tanggallahir',False),
                                jeniskelamin    = request.POST.get('jeniskelamin',False),
                                rt              = request.POST.get('rt',False),
                                alamat          = request.POST.get('alamat',False),

                        )
                        return redirect('atur')
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')

        return render(request,'adminpage/update.html',context)

@login_required(login_url='masuk')
def cari(request):
        data = Tambah.objects.all().order_by('-updated')

        datart=Tambah.objects.values('rt').distinct()

        context = {
                'judul' : 'cari data',
                'datauser'  : data,
                'rtloop'    : datart,
        }
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')
        

        return render(request,'adminpage/cari.html',context)

def carirt(request,rt_id):
        datart= rt_id
        datart1=Tambah.objects.values('rt').distinct()

        data = Tambah.objects.filter(rt=datart).order_by('-updated')
        context = {
                'rtaktif' : datart,
                'judul' : 'cari data',
                'datauser'  : data,
                'rtloop'        : datart1,
        }

        return render(request,'adminpage/carirt.html',context)

@login_required(login_url='masuk')
def printrt(request,rt_id):
        data = Tambah.objects.filter(rt=rt_id).order_by('-id')
        template = get_template('adminpage/print.html')
        user = request.user
        context = {
                'user' : user.username,
                'data' : data,
        }
        html = template.render(context)
        pdf  = render_to_pdf('adminpage/print.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "datart%s.pdf" %(rt_id)
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")



@login_required(login_url='masuk')
def print(request,*args,**kwargs):
        data = Tambah.objects.all().order_by('-id')
        template = get_template('adminpage/print.html')
        user = request.user
        context = {
                'user' : user.username,
                'data' : data,
        }
        html = template.render(context)
        pdf  = render_to_pdf('adminpage/print.html',context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "datawarga%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")



@login_required(login_url='masuk')
def tambahpengumuman(request):
        Pengumuman = TambahPengumuman.objects.all().order_by('-updated')
        context={
                'judul' : 'Tambah Pengumuman',
                'pengumuman' :Pengumuman,

        }

        if 'tambahpengumuman' in request.POST:
                if request.POST["tambahpengumuman"] == "Submit":
                        TambahPengumuman.objects.create(
        			judul 		= request.POST.get('judul',False),
                                deskripsi       = request.POST.get('deskripsi',False),
        			pembuat		= request.POST.get('pembuat',False),
        			kategori	= request.POST.get('kategori',False),
                                isi             = request.POST.get('isi',False),
                        )
                        return redirect('tambahpengumuman')
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')


        return render(request,'adminpage/tambahpengumuman.html',context)

@login_required(login_url='masuk')
def deletepengumuman(request,id_pengumuman):
        data = TambahPengumuman.objects.get(id=id_pengumuman)
        data.delete()

        return redirect('tambahpengumuman')

@login_required(login_url='masuk')
def updatepengumuman(request,id_pengumuman):
        data = TambahPengumuman.objects.get(id=id_pengumuman)
        context = {
                'judul'         : data.judul,
                'isi'           : data.isi,
                'deskripsi'     : data.deskripsi,
        }
        if 'update' in request.POST:
                if request.POST["update"] == "Submit":
                        TambahPengumuman.objects.filter(id=id_pengumuman).update(
        			judul 		= request.POST.get('judul',False),
                                deskripsi       = request.POST.get('deskripsi',False),
        			pembuat		= request.POST.get('pembuat'),
        			kategori	= request.POST.get('kategori',False),
                                isi             = request.POST.get('isi',False),
                                updated          = datetime.now(),
                        )
                        return redirect('tambahpengumuman')
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')

        return render(request,'adminpage/updatepengumuman.html',context)


@login_required(login_url='masuk')
def dokumentasi(request):
        data = Dokumentasi.objects.all()
        context = {
                'datas' : data,
        }
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')


        return render(request,'adminpage/dokumentasi.html',context)


@login_required(login_url='masuk')
def hapusdokumentasi(request,id_dokumentasi):
        data = Dokumentasi.objects.get(id=id_dokumentasi)
        data.delete()

        return redirect('dokumentasi')


@login_required(login_url='masuk')
def tambahdokumentasi(request):
        if 'tambahdokumentasi' in request.POST:
                if request.method =="POST":
                        if request.POST["tambahdokumentasi"] == "Submit":
                                form = TambahDokumentasi(request.POST,request.FILES)
                                if form.is_valid():
                                        form.save()
                                        # data = Dokumentasi.objects.all()
                                        # context = {
                                        #         'datas' : data,
                                        #         }
                                        # return render(request,'adminpage/dokumentasi.html',context)
                                        return redirect('dokumentasi')
        else:
                form = TambahDokumentasi()
        if 'logout' in request.POST:
                if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')

        context = {
                'form' : form,
        }
        return render(request,'adminpage/tambahdokumentasi.html',context)

@login_required(login_url='masuk')
def updatedokumentasi(request,id_dokumentasi):
        update = Dokumentasi.objects.get(id=id_dokumentasi)
        data = {
                'judul'         : update.judul,
                'deskripsi'     : update.deskripsi,
                'gambarutama'   : update.gambarutama,
                'gambar1'       : update.gambar1,
                'gambar2'       : update.gambar2,
                'gambar3'       : update.gambar3,
                'gambar4'       : update.gambar4,
                'gambar5'       : update.gambar5,
        }
        form = TambahDokumentasi(request.POST or None,request.FILES or None,initial = data,instance=update)
        if 'tambahdokumentasi' in request.POST:
                if request.method =="POST":
                        if request.POST["tambahdokumentasi"] == "Submit":
                                form = TambahDokumentasi(request.POST or None,request.FILES or None,initial = data,instance=update)
                                if form.is_valid():
                                        form.save()
                                        # data = Dokumentasi.objects.all()
                                        # context = {
                                        #         'datas' : data,
                                        #         }
                                        # return render(request,'adminpage/dokumentasi.html',context)
                                        return redirect('dokumentasi')
        context = {
                'form' :form,

        }
        if 'logout' in request.POST:
                 if request.method =="POST":
                        if request.POST["logout"] == "Submit":
                                logout(request)
                                messages.error(request,'Logout Berhasil, sampai Jumpa!')
                                return redirect('masuk')


        return render(request,'adminpage/tambahdokumentasi.html',context)