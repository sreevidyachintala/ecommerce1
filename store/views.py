from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from store.forms import Usreg

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password,check_password

from .models import *

from django.contrib import messages
# Create your views here.

def store(request):
	products = Product.objects.all()
	#context = {'products':products}
	return render(request, 'store/store.html', {'products':products})

def cart(request):
	if request.user.is_authenticated:
		customer=request.user.id
		order,complete=Order.objects.get_or_create(customer_id=customer)
		items=order.orderitem_set.all()
		cartitems=order.get_cart_items
	else:
		items=[]
	context={'items':items}
	#context={}
	return render(request , 'store/cart.html' , context)


def addcartview(request, product_id):
	products = models.Product.objects.all()
	if 'product_ids' in request.COOKIES:
		product_ids = request.COOKIES['product_ids']
		counter = product_ids.split('|')
		product_count_in_cart = len(set(counter))
	else:
		product_count_in_cart = 1
	response = render(request, 'store/main.html',{'products': products, 'product_count_in_cart': product_count_in_cart})
	if 'product_ids' in request.COOKIES:
		product_ids = request.COOKIES['product_ids']
		if product_ids == "":
			product_ids = str(product_id)
		else:
			product_ids = product_ids+"|"+str(product_id)
		response.set_cookie('product_ids', product_ids)
	else:
		response.set_cookie('product_ids', product_id)
	product = models.Product.objects.get(id=product_id)
	messages.info(request, product.name + ' added to cart successfully!')
	return response
# def cartview(request):
#     for cart counter
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         counter = product_ids.split('|')
#         product_count_in_cart = len(set(counter))
#     else:
#         product_count_in_cart = 0

#     # fetching product details from db whose id is present in cookie
#     products = None
#     total = 0
#     if 'product_ids' in request.COOKIES:
#         product_ids = request.COOKIES['product_ids']
#         if product_ids != "":
#             product_id_in_cart = product_ids.split('|')
#             products = models.Product.objects.all().filter(id__in=product_id_in_cart)

#             # for total price shown in cart
#             for p in products:
#                 total = total+p.price
#     return render(request, 'EcomApp/cart.html', {'products': products, 'total': total, 'product_count_in_cart': product_count_in_cart})

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)
def validateCustomer(customer):
	error_message=None
	if (not customer.fname):
		error_message="firstname required"
	elif len(customer.fname)<4:
		error_message="firstname name must be 4 chrs"
	elif not customer.lname:
		error_message="lname name required"
	elif len(customer.lname)<4:
		error_message="lastname name must be 4 chrs"
	elif not customer.phone:
		error_message="Phone number required"
	elif len(customer.phone)<10:
		error_message="phone number must be 10 char long"
	elif len(customer.password)<6:
		error_message="password must be 6 char long"
	elif len(customer.email)<5:
		error_message="email must be 5 char long"
	elif customer.isExist():
		error_message="email address already exist"
	return error_message

def registerUser(request):
	PostData=request.POST
	fname=PostData.get('fname')
	lname=PostData.get('lname')
	phone=PostData.get('phone')
	email=PostData.get('email')
	password=PostData.get('password')
	value={'fname':fname,'lname':lname,'phone':phone,'email':email}
	error_message=None
	customer=Customer(fname=fname,lname=lname,phone=phone,email=email,password=password)
	error_message=validateCustomer(customer)
	if not error_message:
		customer.password=make_password(customer.password)
		customer.register()
		return render(request,'store/store.html')
	else:
		data={
			'error':error_message,
			'values':value
			}
		return render(request,"store/signup.html",data)
	#return HttpResponse("success")


def signup(request):
	if request.method == "POST":
		form = Usreg(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"successfully registered please login")
			return redirect('/log')
			#return HttpResponse("Done")
	form = Usreg()
	return render(request,"store/signup.html",{'form':form})


# def login(request):
# 	if request.method == 'GET':
# 		return render(request,"store/login.html")

# 	else:
# 		email=request.POST.get('email')
# 		password=request.POST.get('password')
# 		customer=Customer.get_customer_by_email(email)
# 		error_message=None
# 		if customer:
# 			flag=check_password(password,customer.password)
# 			if flag:
# 				return redirect('/store')
# 			else:
# 				error_message="email or password invalid"
# 		else:
# 			error_message='email or password invalid'
# 		return render(request,'store/login.html',{'error':error_message})

def view1(request):
	p = Product.objects.filter()
	context = {'p':p}
	return render(request,'store/v28.html',context)

@login_required
def dashboard(request):
	return render(request,'store/dashboard.html')

def about(request):
	return render(request,'store/about.html')
def contact(request):
	return render(request,'store/contact.html')

def profile(request):
	return render(request,'store/profile.html')

def addproduct(request):
	products = Product.objects.all()
	context = {'products':products}
	
	return render(request,'store/addproduct.html',context)
	