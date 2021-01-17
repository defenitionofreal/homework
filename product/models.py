from django.db import models
from django.urls import reverse
from django.core import validators
from django.core.exceptions import ValidationError
from main.models import SeoModel
# Create your models here.
class Product(SeoModel):

    STATUS_CHOICES = (
        ('hide', 'Скрыть'),
        ('show', 'Показать'),
    )

    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Максимальный размер не больше %sMB" % str(megabyte_limit))

    title = models.CharField(max_length=250, verbose_name='Название продукта')
    slug = models.SlugField(max_length=250, unique_for_date='created', verbose_name='Url путь')
    img = models.ImageField(upload_to='images/product/', blank=True,
                            verbose_name='Изображения',
                            validators=[validate_image, validators.FileExtensionValidator(allowed_extensions=('jpg', 'jpeg',))],
                            error_messages={'invalid_extension': 'Этот формат не поддерживается. Только jpg'})
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обнавлен')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='show', verbose_name='Статус')

    def get_absolute_url(self):
        return reverse('product:product_detail', args=[self.slug])

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title

class ListTitle(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='productlisttitle')
    title = models.CharField(max_length=150, verbose_name='Заголовок списка')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заголовок списка'
        verbose_name_plural = 'Заголовоки списков'

class ListItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.ForeignKey(ListTitle, on_delete=models.CASCADE, verbose_name='Выбрать заголовок', related_name='productlistitem')
    item = models.CharField(max_length=250, verbose_name='Пункт списка')

    def __str__(self):
        return self.item

    class Meta:
        verbose_name = 'Пункт списка'
        verbose_name_plural = 'Пункты списков'
