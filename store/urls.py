from django.urls import path

from . import views

from django.contrib.auth import views as v

urlpatterns = [
	#Leave as empty string for base url
	path('',views.store, name="store"),
	path('cart/',views.cart, name="cart"),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	
	path('checkout/', views.checkout, name="checkout"),
	path('signup/',views.signup,name='signup'),
	
	#path('login/',views.login,name='login'),
	path('view1/',views.view1,name='v28'),
	path('profile/',views.profile,name='profile'),
	path('addpro/',views.addproduct,name="addpro"),
	
	path('dsh/',views.dashboard,name='dsh'),
	path('log/',v.LoginView.as_view(template_name='store/login1.html'),name='log'),
	path('lgo/',v.LogoutView.as_view(template_name='store/logout.html'),name='lgot'),

]