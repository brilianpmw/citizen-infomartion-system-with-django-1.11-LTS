from django import forms
from .models import Dokumentasi

class TambahDokumentasi(forms.ModelForm):
    class Meta:
        model = Dokumentasi
        fields=['judul','deskripsi','gambarutama','gambar1','gambar2','gambar3','gambar4','gambar5']


    # judul       = forms.CharField(max_length=255)
    # deskripsi   = forms.CharField(max_length=255)
    # gambarutama = forms.ImageField()
    # gambar1     = forms.ImageField()
    # gambar2     = forms.ImageField()
    # gambar3     = forms.ImageField()
    # gambar4     = forms.ImageField()
    # gambar5     = forms.ImageField()   
