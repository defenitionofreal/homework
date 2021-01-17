from django.shortcuts import render, redirect
from .models import *
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from product.models import Product
# Create your views here.
def index(request):
    main = Main.objects.all()
    img = SliderImage.objects.all()
    text = Text.objects.all()
    map = Map.objects.all()
    products = Product.objects.filter(status='show')

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            try:
                send_mail(name, from_email, 'iwebpro.ru@mail.ru', ['test@codestudio.org'], fail_silently=False,)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('success')

    context = {'main': main, 'img': img, 'text': text, 'map': map, 'products': products, 'form': form,}
    return render(request, 'index.html', context)

def success(request):
    return HttpResponse('Сообщение отправленно.')
