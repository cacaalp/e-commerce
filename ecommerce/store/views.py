from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def store(request):
	products = Product.objects.filter(status=1).values('title', 'price', 'image', 'slug')
	# select title, price, image, slug from Products where status = 1
	# select_releated vs prefetch_releated => SQL karşılığı Join
	# SQL tarafında SP yazma ve onu django yani app side çağırma
	context = {
		'products': products
	}
	
	return render(request, 'store/store.html', context)


def categories(request):
	all_categories = Category.objects.all()

	data = {'all_categories': all_categories}
	
	return data


def get_product_by_category(request, category_slug=None):
	
	category = get_object_or_404(Category, slug=category_slug)
	
	products = Product.objects.filter(category=category)
	
	context = {
		'category': category,
		'products': products
	}
	
	return render(request, 'store/get_product_by_category.html', context)


def product_detail(requrst, product_slug):
	product = get_object_or_404(Product, slug=product_slug)
	
	context = {
		'product': product
	}
	
	return render(requrst, 'store/product_detail.html', context)