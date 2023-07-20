
from django.urls import path
from . import views

urlpatterns = [
	path('', views.store, name='store'),
	
	path('search/<slug:category_slug>/',
	     views.get_product_by_category,
	     name='get_product_by_category'),
	
	path('product/<slug:product_slug>/',
	     views.product_detail,
	     name='product_detail')
]