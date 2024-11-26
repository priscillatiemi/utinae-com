from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count
from core.models import Product, Category, Vendor, CartOrder, CartOrderItems, WishList, ProductImages, ProductReview, Address


# Create your views here.

def index(request):
    # products = Product.objects.all().order_by("-id")
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'core/index.html', context)

def product_list_view(request):
    products = Product.objects.filter(product_status="published")
    context = {
        "products": products
    }
    return render(request, 'core/product-list.html', context)

def category_list_view(request):
    categories = Category.objects.all().annotate(product_count=Count("category"))
    context = {
        "categories": categories
    }

    return render(request, 'core/category-list.html', context)

def category_product_list_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status="published", category=category)
    context = {
        "category": category,
        "products": products
    }
    return render(request, "core/category-product-list.html", context)

def vendor_list_view(request):
    vendor = Vendor.objects.all()
    context = {
        "vendor":vendor,
    }
    return render(request,"core/vendor-list.html", context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_object_or_404(Product, pid=pid)
    
    context = {
        "product": product,
    }
    return render(request, "core/product-detail.html", context)

