from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Basket, ProductAttribute
from django.shortcuts import HttpResponseRedirect


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "catalog/index.html", {"products": products, "categories": categories, })


def category(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id)
    return render(request, "catalog/category.html", {"products": products, "categories": categories})


def basket_add(request, product_id):
    Basket.create_or_update(session=request.session.session_key, product_id=product_id)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_del(request, product_id):
    Basket.basket_delete(session=request.session.session_key, product_id=product_id)
    return HttpResponseRedirect("/home/basket")


def basket_quantity(request, product_id):
    Basket.edit_quantity(session=request.session.session_key, product_id=product_id)
    return HttpResponseRedirect('/home/basket')


def product_page(request, category_id, product_id):
    product = Product.objects.get(pk=product_id, category_id=category_id)
    info = ProductAttribute.objects.filter(product_id=product_id)
    return render(request=request, template_name="catalog/product.html", context={"product" : product, "info": info})


def basket_page(request):
    baskets = Basket.objects.filter(session=request.session.session_key).order_by('id')
    total_price = Basket.total_sum(session=request.session.session_key)
    return render(request=request, template_name="catalog/basket.html", context={"baskets" : baskets, "total_price": total_price})

