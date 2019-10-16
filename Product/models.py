from django.db import models
from django.urls import reverse


class Category(models.Model):
	name = models.CharField(max_length=20)
	# parent = models.ForeignKey('self',blank=True, null=True ,
	# 								related_name='subcategory',on_delete="SET_NULL")

	class Meta:
		verbose_name_plural = "categories"
	
	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse ("Product:category-detail", kwargs={'pk':self.pk})

class Product(models.Model):
	name     = models.CharField(max_length=20,null=True,unique=True)
	code 	 = models.CharField(max_length=20,null=True,unique=True)
	price	 = models.DecimalField(decimal_places=2,max_digits=8)
	quantity = models.IntegerField()
	category = models.ManyToManyField(Category)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse ("Product:category-detail", kwargs={'pk':self.pk})