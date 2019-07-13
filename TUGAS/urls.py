
from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name='home'),
    url(r'^pengumuman/',include('pengumuman.urls'),name='bagianpengumuman'),
    url(r'^adminpage/',include('adminpage.urls')),
    url(r'^dokumentasi/', include('dokumentasi.urls'),name='bagiandokumentasi'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
