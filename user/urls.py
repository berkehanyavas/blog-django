from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('uyeol/',views.uyeol,name="uyeol"),
    path('giris/',views.giris,name="giris"),
    path('cikis/',views.cikis,name="cikis"),
]