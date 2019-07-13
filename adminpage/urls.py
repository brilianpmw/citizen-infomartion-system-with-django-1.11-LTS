from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #url(r'^testdoang/',views.testdoang),
    url(r'^atur/cari/printrt/(?P<rt_id>[0-9]+)$',views.printrt,name="printrt"),
    url(r'^atur/cari/print',views.print,name="print"),
    url(r'^atur/cari/rt/(?P<rt_id>[0-9]+)$',views.carirt,name="carirt"),
    url(r'^atur/delete/(?P<id_user>[0-9]+)$',views.delete,name="delete"),
    url(r'^atur/cari',views.cari,name="cari"),
    url(r'^atur/update/(?P<id_user>[0-9]+)$',views.update,name="update"),
    url(r'^dokumentasi/delete/(?P<id_dokumentasi>[0-9]+)$',views.hapusdokumentasi,name="hapusdokumentasi"),
    url(r'^dokumentasi/update/(?P<id_dokumentasi>[0-9]+)$',views.updatedokumentasi,name="updatedokumentasi"),
    url(r'^tambahpengumuman/update/(?P<id_pengumuman>[0-9]+)$',views.updatepengumuman,name="updatepengumuman"),
    url(r'^tambahpengumuman/(?P<id_pengumuman>[0-9]+)$',views.deletepengumuman,name="deletepengumuman"),
    url(r'^dokumentasi/tambah',views.tambahdokumentasi,name="tambahdokumentasi"),    
    url(r'^tambahpengumuman/',views.tambahpengumuman,name="tambahpengumuman"),
    url(r'^dokumentasi/',views.dokumentasi,name="dokumentasi"),
    url(r'^masuk/',views.masuk,name="masuk"),
    url(r'^atur/',views.atur,name="atur"),
    url(r'^$',views.index,name="index"),

    
] 
