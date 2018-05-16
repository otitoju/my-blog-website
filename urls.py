#from django.conf.urls import url
#from django.contrib import admin
from django.urls import path

from .views import(
    post_create,
    post_home,
    post_detail,
    post_update,
    post_list,
    post_delete,

)


urlpatterns = [
    path('', post_list, name='list'),
    path('create/', post_create),
    path('(?P<id>\d+)/delete', post_delete),
    path('home/', post_home),
    path('detail/', post_detail, name='detail'),
    path('(?P<id>\d+)/edit', post_update,name='update' ),

 ]