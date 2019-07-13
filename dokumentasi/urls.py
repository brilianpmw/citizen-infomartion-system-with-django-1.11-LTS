from django.conf.urls import url
from . import views

urlpatterns = [
 url(r'^(?P<slugInput>[\w-]+)/$',views.detail,name='detail'),
 url(r'^$',views.index),

]
