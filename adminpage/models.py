from django.db import models
from datetime import datetime
from django.utils.text import slugify




class Tambah(models.Model):
    nik             =models.CharField(max_length=50)
    nama            =models.CharField(max_length=25)
    tanggallahir    =models.DateTimeField(default='')
    jeniskelamin    =models.CharField(max_length=10)
    rt              =models.CharField(max_length=3)
    alamat          =models.TextField()
    updated         =models.DateTimeField(auto_now=True)

    def __str__(self):
	
        return "{}. {}".format(self.id, self.nama)

class TambahPengumuman(models.Model):
    judul		= models.CharField(max_length=255)
    deskripsi   = models.CharField(max_length=1000)
    isi         = models.TextField()
    kategori    =models.CharField(max_length=255)
    dibuat      = models.DateTimeField(auto_now_add=True)
    updated     =models.DateTimeField(auto_now=True)
    pembuat     =models.CharField(max_length=50,default='a')
    slug        = models.SlugField(blank=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.judul)
        super(TambahPengumuman,self).save(*args,**kwargs)

    def __str__(self):
        return "{}.{}".format(self.id,self.judul)

class Dokumentasi(models.Model):
    judul       = models.CharField(max_length=255)
    deskripsi   = models.CharField(max_length=255)
    gambarutama = models.ImageField(blank=True,null=True,upload_to='images/')
    gambar1     = models.ImageField(blank=True,null=True,upload_to='images/')
    gambar2     = models.ImageField(blank=True,null=True,upload_to='images/')
    gambar3     = models.ImageField(blank=True,null=True,upload_to='images/')
    gambar4     = models.ImageField(blank=True,null=True,upload_to='images/')
    gambar5     = models.ImageField(blank=True,null=True,upload_to='images/')
    slug        = models.SlugField(blank=True,editable=False)

    def save(self,*args,**kwargs):
        self.slug=slugify(self.judul)
        super(Dokumentasi,self).save(*args,**kwargs)

    def __str__(self):
        return "{}.{}".format(self.id,self.judul)


    


