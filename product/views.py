from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import *

# Create your views here.

def product_detail(request, title):

    product = get_object_or_404(Product, slug=title, status='show')
    list = ListTitle.objects.filter(product=product)
    item = ListItem.objects.filter(product=product)

    context = {'product': product,
               'list': list,
               'item': item,
               }
    return render(request, 'product.html', context)


