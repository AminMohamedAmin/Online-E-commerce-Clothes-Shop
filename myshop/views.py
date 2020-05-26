from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Category, Product, Product_Review, Product_Info
from cart.forms import CartAddProductForm



def product_list(request):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }
    return render(request, 'product.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    produc = Product.objects.filter(available=True, category=product.category)

    if Product_Info.objects.filter(productInfo_id=id).exists() == True:
        pinfo = Product_Info.objects.get(productInfo_id=id)
        psize = pinfo.Sizes.split(",")
        pcolor = pinfo.Colors.split(",")
    else:
        pinfo = None
        psize = None
        pcolor = None

    preview = Product_Review.objects.filter(productreview_id=id)
    if preview.exists() == True:
        ppreview = Product_Review.objects.filter(productreview_id=id)
    else:
        ppreview = None

    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'produc':produc,
        'psize':psize,
        'pcolor':pcolor,
        'pinfo':pinfo,
        'preview':preview,
        'ppreview': ppreview,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'product-detail.html', context)

def AddReview(request, n):
    rating = request.POST['rating']
    review = request.POST['review']
    name = request.POST['name']
    email = request.POST['email']
    new = Product_Review()
    old = Product.objects.get(name=n)
    new.rating = rating
    new.review = review
    new.user = name
    new.email = email
    new.productreview = old
    new.save()
    return HttpResponseRedirect('../../../myshop/product_detail/%d/'%old.id)