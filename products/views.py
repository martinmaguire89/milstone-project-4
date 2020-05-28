from django.shortcuts import render
from .models import Product, Cases


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def cases(request):
    cases = Cases.objects.all()
    return render(request, "cases.html", {"cases": cases})
