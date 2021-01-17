from django.urls import path, include
from . import views

app_name = 'product'

urlpatterns = [
    path('<slug:title>/', views.product_detail, name='product_detail'),
]