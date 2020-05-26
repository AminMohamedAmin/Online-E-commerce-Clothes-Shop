from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('addreview/<str:n>/', views.AddReview, name='addreview'),
]