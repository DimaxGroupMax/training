from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Products


def catalog(request, category_slug) -> HttpResponse:
 if category_slug == 'all':
  goods = Products.objects.all()
 else:
  goods = Products.objects.filter(category__slug=category_slug)
 context = {
  'title': 'Каталог товаров',
  'goods': goods
 }
 return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug) -> HttpResponse:
 product = Products.objects.get(slug=product_slug)
 context = {
  "product": product
 }
 return render(request, 'goods/product.html', context=context)

