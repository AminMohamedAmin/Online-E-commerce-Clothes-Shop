from django.conf import settings
from myshop.models import Product

class Wish(object):
	"""docstring for Wish"""

	def __init__(self, request):
		"""initalize the wishlist"""
		self.session = request.session
		wish = self.session.get(settings.WISH_SESSION_ID)

		if not wish:
			wish = self.session[settings.WISH_SESSION_ID] = {}
		self.wish = wish

	def add(self,product):
		product_id = str(product.id)

		if product_id not in self.wish:
			self.wish[product_id] = {'price':str(product.price)}

		self.save()

	def save(self):
		self.session[settings.WISH_SESSION_ID] = self.wish
		self.session.modified = True

	def remove(self,product):
		product_id = str(product.id)
		if product_id in self.wish:
			del self.wish[product_id]
			self.save()

	def __iter__(self):
		product_ids = self.wish.keys()
		products = Product.objects.filter(id__in=product_ids)
		for product in products:
			self.wish[str(product.id)]['product'] = product

		for item in self.wish.values():
			item['price'] = item['price']
			item['Image1'] = item['Image1']
			yield item


	def clear(self):
		del self.session[settings.WISH_SESSION_ID]
		self.session.modified = True