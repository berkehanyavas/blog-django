from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path('kontrolpaneli/',views.dashboard,name="kontrolpaneli"),
    path('makaleekle/',views.makaleekle,name="makaleekle"),
    path('makale/<int:id>',views.makaledetay,name="detay"),
    path('guncelle/<int:id>',views.guncelle,name="guncelle"),
    path('sil/<int:id>',views.sil,name="sil"),
    path('',views.makaleler,name="makaleler"),
    path('comment/<int:id>',views.yorumekle,name="comment"),

]