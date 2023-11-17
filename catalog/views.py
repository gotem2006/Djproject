from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category, Basket
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


def basket(request):
    baskets = Basket.objects.filter(session=request.session.session_key)
    content = ""
    for i in baskets:
        content += f"{i.product.name}\n"

    return HttpResponse(content)


def basket_del(request, product_id):
    Basket.basket_delete(session=request.session.session_key, product_id=product_id)
    return HttpResponseRedirect("/")


def basket_quantity(request, product_id):
    Basket.edit_quantity(session=request.session.session_key, product_id=product_id)
    return HttpResponseRedirect('/')
