from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('add', views.add, name='add'),
	path('create_order/', views.createOrder, name='create_order'),
	path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
	path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
	path('register/', views.registerPage, name='register'),
	path('login/', views.loginPage, name='login'),
	path('logout/', views.logoutPage, name='logout'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('products/', views.products, name='products'),
	path('customer/<str:pk_test>/', views.customer, name='customer'),
	path('import_csv/', views.import_csv, name='import_csv'),
]

