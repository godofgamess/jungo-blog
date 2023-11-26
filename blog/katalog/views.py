from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, News

def demon(request):
#    return HttpResponse('<h1>Главная</h1>')
    return render(request, 'katalog/demon.html')

def home(request):
    li = Product.objects.all()
    blog_list = News.objects.all()
    content = {
        'list': li,
        'blog_list': blog_list
    }
    return render(request, 'katalog/index.html', context=content )
