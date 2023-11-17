from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path('<int:category_id>/', category, name="category"),
    path('baket/add/<int:product_id>/', basket_add, name="basket_add"),
    path('basket/del/<int:product_id>/', basket_del, name="basket_del"),
    path('basket/minus/<int:product_id>', basket_quantity, name="basket_quantity"),
]
