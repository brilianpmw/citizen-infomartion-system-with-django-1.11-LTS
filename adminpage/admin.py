from django.contrib import admin

# Register your models here.
from .models import Tambah,TambahPengumuman,Dokumentasi

admin.site.register(Tambah)
admin.site.register(TambahPengumuman)
admin.site.register(Dokumentasi)
