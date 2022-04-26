from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse

import article
from .forms import ArticleForm
from django.contrib import messages
from .models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,"index.html")

def hakkinda(request):
    return render(request,"hakkinda.html")

@login_required(login_url="user:giris")
def dashboard(request):
    makaleler = Article.objects.filter(author = request.user)
    context = {
        "makaleler": makaleler
    }
    return render(request,"kontrolpaneli.html",context)

def makaleler(request):
    arama = request.GET.get("keyword")
    
    if arama:
        makaleliste = Article.objects.filter(title__contains = arama)
        return render(request,"makaleler.html",{"makaleler":makaleliste})
    
    makaleliste = Article.objects.all()
    return render(request,"makaleler.html",{"makaleler":makaleliste})

@login_required(login_url="user:giris")
def makaleekle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.author = request.user
        makale.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("index")
    return render(request,"makaleekle.html",{"form":form})

def makaledetay(request,id):
    #makale = Article.objects.filter(id = id).first()
    makale = get_object_or_404(Article,id = id)
    comments = makale.comments.all()
    return render(request,"detay.html",{"makale":makale,"comments":comments})

@login_required(login_url="user:giris")
def guncelle(request,id):
    makale = get_object_or_404(Article,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance = makale)
    if form.is_valid():
        makale = form.save(commit=False)
        makale.author = request.user
        makale.save()
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("article:kontrolpaneli")

    return render(request,"guncelle.html",{"form":form})

@login_required(login_url="user:giris")
def sil(request,id):
    makale = get_object_or_404(Article,id=id)
    makale.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("article:kontrolpaneli")

def yorumekle(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newcomment = Comment(comment_author=comment_author, comment_content=comment_content)
        newcomment.article = article
        newcomment.save()
    return redirect(reverse("article:detay",kwargs={"id":id}))