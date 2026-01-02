from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        "title": "Главная",
        "content": "Контент главной страницы",
        "list_items": ["first 1", "second 2"],
        "dict_items": {"One": 1},
        "is_authenticated": True,
    }
    return render(request, "main/index.html", context)

def about(request):
    return HttpResponse("About page")
