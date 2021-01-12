from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
	#user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
	fname = models.CharField(max_length=200,null=True)
	lname=models.CharField(max_length=50,null=True)
	phone=models.CharField(max_length=10,null=True)
	email = models.EmailField(max_length=200,null=True)
	password=models.CharField(max_length=20,null=True)


	def register(self):
		self.save()

	def isExist(self):
		if Customer.objects.filter(email=self.email):
			return True
		return False

	@staticmethod
	def get_customer_by_email(email):
		try:
			return Customer.objects.get(email=email)
		except:
			return False




class Product(models.Model):
	name=models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True,blank=True)
	image = models.ImageField(null=True,blank=True)
	#product_status=models.BooleanField(default=False)

	@staticmethod
	def get_products_by_id(ids):
		return Product.objects.filter(id__in =ids)

	def __str__(self):
		return self.name

class Order(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
	date_ordered=models.DateTimeField(auto_now_add=True)
	complete = models.CharField(max_length=100,null=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
	product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
	order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	quantity=models.IntegerField(default=0,null=True,blank=True)
	date_added=models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
	customer=models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True)
	order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
	address=models.CharField(max_length=200,null=False)
	city=models.CharField(max_length=200,null=False)
	state= models.CharField(max_length=200,null=False)
	pincode=models.CharField(max_length=200,null=False)
	date_added=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address