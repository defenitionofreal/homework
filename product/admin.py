from django.contrib import admin
from .models import *
# Register your models here.

class ListTitleAdmin(admin.StackedInline):
    model = ListTitle
    extra = 1
    max_num = 3

class ListItemAdmin(admin.StackedInline):
    model = ListItem
    extra = 3

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('title', 'status', 'created', 'updated',)
    list_filter = ('title', 'status', 'created', 'updated',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created'
    ordering = ('status', 'created',)

    inlines = [ListTitleAdmin, ListItemAdmin,]

    fieldsets = (
        ('Название продукта', {
            'fields': ('title',)
        }),
        ('Сео теги', {
            'fields': ('seo_title', 'seo_keywords', 'seo_description',)
        }),
        ('Путь URL продукта', {
            'fields': ('slug',)
        }),
        ('Изображение продукта', {
            'fields': ('img',)
        }),

        ('Статус', {
            'fields': ('status',)
        }),
    )

admin.site.register(Product, ProductAdmin)