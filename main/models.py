from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError
# Create your models here.


class SeoModel(models.Model):
    seo_title = models.CharField('Title', blank=True, max_length=250)
    seo_description = models.CharField('Description', blank=True, max_length=250)
    seo_keywords = models.CharField('Keywords', blank=True, max_length=250)

    def get_seo_title(self):
        if self.seo_title:
            return self.seo_title
        return ''

    def get_seo_description(self):
        if self.seo_description:
            return self.seo_description
        return ''

    def get_seo_keywords(self):
        if self.seo_keywords:
            return self.seo_keywords
        return ''

    class Meta:
        abstract = True


class Main(SeoModel):
    title = models.CharField(max_length=250, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return self.title


class SliderImage(models.Model):
    def validate_image(fieldfile_obj):
        filesize = fieldfile_obj.file.size
        megabyte_limit = 2.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Максимальный размер не больше %sMB" % str(megabyte_limit))

    page = models.ForeignKey(Main, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/slider/',
                               verbose_name='Картинка',
                               validators=[validate_image, validators.FileExtensionValidator(allowed_extensions=('jpg','jpeg',))],
                               error_messages={'invalid_extension': 'Этот формат не поддерживается. Только jpg'})



    class Meta:
        verbose_name = 'Изображения слайдера'
        verbose_name_plural = 'Изображения слайдера'

    def __str__(self):
        return self.page.title

class Text(models.Model):
    page = models.ForeignKey(Main, default=None, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст', blank=True)

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текст'

class Map(models.Model):
    page = models.ForeignKey(Main, default=None, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name='Широта', blank=True)
    lon = models.FloatField(verbose_name='Долгота', blank=True)

    class Meta:
        verbose_name = 'Кординаты карты'
        verbose_name_plural = 'Кординаты карты'


