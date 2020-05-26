from django.contrib import admin
from .models import Category,Product,Product_Info, Product_Review
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	'''
		Admin View for Category
	'''
	list_display = ('name','slug',)
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
	'''
		Admin View for Product
	'''
	list_display = ('name','category','price','stock','available','created','updated',)
	list_filter = ('available','created','updated','category',)
	list_editable = ('price','stock','available',)
	prepopulated_fields = {'slug':('name',)}


admin.site.register(Product, ProductAdmin)


class ProductInfoAdmin(admin.ModelAdmin):
	'''
		Admin View for Product_Info
	'''
	list_display = ('productInfo','created')
	list_filter = ('created','productInfo',)


admin.site.register(Product_Info, ProductInfoAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
	'''
		Admin View for Product_Review
	'''
	list_display = ('productreview','rating','review','user','email','created',)
	list_filter = ('created','productreview',)
	list_editable = ('review','rating','user',)


admin.site.register(Product_Review, ProductReviewAdmin)


