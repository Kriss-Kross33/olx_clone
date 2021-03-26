from django.shortcuts import render
from .models import Product, ProductImages

# Create your views here

def productList(request):
    productList = Product.objects.all()
    context = {'product_list': productList}
    template = 'product/product_list.html'
    return render(request, template, context)

def productDetail(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    product_images = ProductImages.objects.filter(product=product)
    context = {'product': product, 'product_images': product_images}
    template = 'product/product_detail.html'
    return render(request, template, context)