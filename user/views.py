from django.shortcuts import render,redirect
from flask import render_template
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.

def uyeol(request):
    if request.user.is_authenticated:
        messages.info(request,"Öncelikle çıkış yapmalısınız.")
        return redirect("index")
    else:
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            newuser = User(username = username)
            newuser.set_password(password)
            
            newuser.save()
            
            login(request,newuser)
            messages.success(request,"Başarıyla kayıt oldunuz.")
            
            return redirect("index")
        context = {
            "form" : form
        }
        return render(request,"uyeol.html",context)

def giris(request):
    if request.user.is_authenticated:
        messages.info(request,"Öncelikle çıkış yapmalısınız.")
        return redirect("index")
    else:
        form = LoginForm(request.POST or None)
        context = {
            "form" : form
        }
        
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username,password=password)
            
            if user is None:
                messages.info(request,"Kullanıcı adı veya şifre yanlış!")
                return render(request, "giris.html",context)
        
            messages.success(request,"Başarıyla giriş yaptınız.")
            login(request,user)
            return redirect("index")
            
        return render(request,"giris.html",context)

def cikis(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Başarıyla Çıkış Yaptınız.")
        return redirect("index")
    else:
        messages.info(request,"Öncelikle giriş yapmalısınız.")
        return redirect("index")

