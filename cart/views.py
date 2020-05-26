from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product
from .models import ShippingCountry
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm


@require_POST
def cart_add(request,product_id):
	cart = Cart(request)
	product = get_object_or_404(Product,id=product_id)

	color = request.POST['colorr']
	size = request.POST['sizee']


	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(
			product=product,
			color=color,
			size=size,
			quantity=cd['quantity'],
			update_quantity=cd['update']
			)
	return redirect('cart:cart_detail')


def cart_remove(request,product_id):
	cart = Cart(request)
	product = get_object_or_404(Product,id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
	cart = Cart(request)

	countryshipping = ShippingCountry.objects.all()

	shippingcountry = request.POST.get('ship', False)

	shco = ShippingCountry.objects.filter(country=shippingcountry)

	# for item in cart:
	# 	item['update_quantity_form'] = CartAddProductForm(initial={'quantity':item['quantity'],'update':True})

	coupon_apply_form = CouponApplyForm()
	context = {
		'cart': cart,
		'countryshipping': countryshipping,
		'shippingcountry':shippingcountry,
		'shco':shco,
		'coupon_apply_form':coupon_apply_form
	}
	return render(request,'shoping-cart.html',context)
