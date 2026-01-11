from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from goods.models import Categories

def index(request):


    context = {
        "title": "Главная",
        "content": "Магазин мебели HOME",
    }
    return render(request, "main/index.html", context)

def about(request):
    context = {
        "title": "О нас",
        "content": "О нас",
        "text_on_page": "Текст на странице о интернет магазине",
    }
    return render(request, "main/about.html", context)
