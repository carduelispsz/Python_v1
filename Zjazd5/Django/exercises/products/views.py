from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product


# def products_list(request):
#     products = Product.objects.all()
#     return HttpResponse(products)

def products_list(request):
    products = Product.objects.all()
    return render(
        request=request,
        context={'products':products},
        template_name = "products_list.html"
    )

def products_list_mod(request):
    products = Product.objects.all()
    output = ""
    for prod in products:
        output += str(prod) + "<br>" #<br> to break line
    return HttpResponse(output)

def product_details(request, id):
    product = Product.objects.get(pk=id)
    output = f"Product: {product.id}<br>"
    output += f"Product: {product.name}<br>"
    output += f"Product: {product.description}<br>"
    return HttpResponse(output)

