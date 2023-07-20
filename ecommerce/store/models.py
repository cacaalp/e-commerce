from django.db import models
from django.urls import reverse


class Status(models.Choices):
	Active = 1
	Modified = 2
	Passive = 3



class Category(models.Model):
	name = models.CharField(max_length=250, db_index=True)
	slug = models.SlugField(max_length=250, unique=True)
	create_date = models.DateField(auto_now_add=True, editable=False)
	status = models.IntegerField(default=Status.Active.value, editable=False)
	
	class Meta:
		verbose_name_plural = 'categories'
		
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('get_product_by_category', args=[self.slug])


class Product(models.Model):
	title = models.CharField(max_length=250, db_index=True)
	brand = models.CharField(max_length=250, default='un-brand')
	description = models.TextField(blank=True)
	price = models.DecimalField(max_digits=4, decimal_places=2)
	slug = models.SlugField(max_length=250)
	status = models.IntegerField(default=Status.Active.value, editable=False)
	# pip install Pillow modülünü yüklemeyi unutmayın resim işlemleri için
	# venv'nin bulunduğu dizine geçmeyi unutmayın
	image = models.ImageField(upload_to='images/')
	category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
	
	class Meta:
		verbose_name_plural = 'products'
	
	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('product_detail', args=[self.slug])