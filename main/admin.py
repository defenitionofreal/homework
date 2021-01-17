from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.

class SliderImageAdmin(admin.StackedInline):
    model = SliderImage

class TextAdmin(admin.StackedInline):
    model = Text
    extra = 1
    max_num = 1

class MapAdmin(admin.StackedInline):
    model = Map
    extra = 1
    max_num = 1

class MainAdmin(admin.ModelAdmin):
    model = Main
    inlines = [SliderImageAdmin, TextAdmin, MapAdmin]
    fieldsets = (
        ('Заголовок', {
            'fields': ('title',)
        }),
        ('Сео теги', {
            'fields': ('seo_title', 'seo_keywords', 'seo_description',)
        }),
    )

    # This will help you to disbale add functionality
    #def has_add_permission(self, request):
    #    return False

    # This will help you to disable delete functionaliyt
    #def has_delete_permission(self, request, obj=None):
    #    return False

    # This will help you to disable change functionality
    #def has_change_permission(self, request, obj=None):
    #    return False


admin.site.register(Main, MainAdmin)

# hide
admin.site.unregister(User)
admin.site.unregister(Group)