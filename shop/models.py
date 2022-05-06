from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone

'''
Бир категорияга канча продукт уланганын корсо болот экен!

related_name

a = Category.objects.get(title='Sport')
>>> a
<Category: Sport>
>>> a.product_set.all()
<QuerySet [<Product: Перчатки>, <Product: Сноуборд>, <Product: Теннис>]>

Men
Women
Sport
Electronic
'''


class Comment(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100)
    is_admin = models.BooleanField(default=False, verbose_name='Вы админ?')
    website = models.CharField(max_length=150, blank=True)
    comment = models.TextField(verbose_name='Комментарий')
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='Comment/%Y/%m/%d', blank=True, verbose_name='Фото')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Названия')
    image = models.ImageField(upload_to='Product/photo/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    new_price = models.FloatField(verbose_name='Новая цена', validators=[MinValueValidator(1)])
    old_price = models.FloatField(verbose_name='Старая цена', validators=[MinValueValidator(1)])
    pub_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата публикации')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1, verbose_name='Категория')
    watch = models.IntegerField(verbose_name='Просмотры', validators=[MinValueValidator(1)])

    # wishlist = models.idontknow(max_length=10)
    # basket = models.ManyToManyRel('Category')
    # favorite = models.ManyToManyRel('Category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100)
    profession = models.CharField(max_length=100, verbose_name='Профессия')
    company = models.CharField(max_length=100, verbose_name='Компания')
    message = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='Customer/%Y/%m/%d', blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Review(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(max_length=100)
    review = models.TextField(verbose_name='Комментарий')
    rating = models.IntegerField(verbose_name='Рейтинг', validators=[MinValueValidator(1), MaxValueValidator(5)])
    pub_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    image = models.ImageField(upload_to='Review/%Y/%m/%d', blank=True, verbose_name='Фото')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    product = models.ManyToManyField(Product, )

    def __str__(self):
        return self.product
