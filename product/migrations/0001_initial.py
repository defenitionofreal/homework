# Generated by Django 3.1.5 on 2021-01-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название продукта')),
                ('slug', models.SlugField(max_length=250, unique_for_date='created', verbose_name='Url путь')),
                ('img', models.ImageField(blank=True, upload_to='images/product/', verbose_name='Изображения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обнавлен')),
                ('status', models.CharField(choices=[('hide', 'Скрыть'), ('show', 'Показать')], default='show', max_length=10, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('-created',),
            },
        ),
    ]
