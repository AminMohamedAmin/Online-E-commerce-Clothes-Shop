from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse

from cart.models import ShippingCountry
from .forms import OrderCreateForm
from .models import OrderItem, order
from cart.cart import Cart

############### pdf ####################
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint
#########################################

def order_create(request):
	cart = Cart(request)

	money = request.POST.get('money', False)

	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			if cart.coupon:
				order.coupon = cart.coupon
				order.discount = cart.coupon.discount
			order.save()
			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity'])

			cart.clear()
			context = {
				'order':order,
				'money':money,
			}
			# request.session['order_id'] = order.id
			# return redirect(reverse('payment:process'))
			return render(request,'order/done.html',context)

	else:
		form = OrderCreateForm()
	context = {
		'cart':cart,
		'form':form,
		'money': money,
	}
	return render(request, 'order/order.html', context)

####################### pdf #######################
@staff_member_required
def admin_order_pdf(request,order_id):
	Order = get_object_or_404(order,id=order_id)
	html = render_to_string('order/pdf.html',{'order':Order})
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'filename="order_{}.pdf"'.format(Order.id)
	weasyprint.HTML(string=html).write_pdf(response,stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
	return response
#######################################################