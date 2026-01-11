from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        'title': 'Каталог товаров',
        'goods':  goods
    }
    return render(request, 'goods/catalog.html', context=context)

def product(request, product_slug=False)-> HttpResponse:

    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product
    }
    return render(request, 'goods/product.html', context=context)
