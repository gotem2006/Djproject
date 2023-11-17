from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название категории')
    description = models.CharField(max_length=200, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=80, verbose_name='Название товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quntity = models.PositiveIntegerField(default=0)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='product_images/%Y-%m-%d/', verbose_name='Фотографии товара', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, related_name='attributes', db_index=True, verbose_name='Товар',
                                on_delete=models.CASCADE)
    attribute_name = models.CharField(max_length=80, verbose_name='Название характеристики')
    attribute_value = models.CharField(max_length=80, verbose_name='Значение характеристики')

    class Meta:
        verbose_name = 'Характеристика'
        verbose_name_plural = 'Характеристики'


class Basket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qauntity = models.PositiveSmallIntegerField(default=0)
    session = models.CharField(max_length=40, null=True)

    @classmethod
    def create_or_update(self, product_id, session):
        baskets = Basket.objects.filter(session=session, product_id=product_id)
        if baskets.exists():
            basket = baskets.first()
            basket.qauntity += 1
            basket.save()
        else:
            basket = Basket.objects.create(session=session, product_id=product_id, qauntity=1)

    @classmethod
    def basket_delete(self, session, product_id):
        basket = Basket.objects.get(session=session, product_id=product_id)
        basket.delete()

    @classmethod
    def edit_quantity(self, session, product_id):
        basket = Basket.objects.get(session=session, product_id=product_id)
        if basket.qauntity == 1:
            basket.delete()
        else:
            basket.qauntity = basket.qauntity - 1
            basket.save()

    def sum(self):
        return self.qauntity * self.product.price

    def __str__(self):
        return f'Корзина для {self.session}'
