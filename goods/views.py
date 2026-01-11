
from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from goods.models import Products
from django.core.paginator import Paginator, Page


def catalog(request, category_slug, page=1) -> HttpResponse:
 if category_slug == 'all':
  goods = Products.objects.all()
 else:
  goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

 paginator = Paginator(goods, 3)
 current_page: Page = paginator.page(page)

 context = {
  'title': 'Каталог товаров',
  'goods': current_page,
  'slug_url': category_slug,
 }
 return render(request, 'goods/catalog.html', context=context)


def product(request, product_slug) -> HttpResponse:
     product = Products.objects.get(slug=product_slug)
     context = {
      "product": product
     }
     return render(request, 'goods/product.html', context=context)

