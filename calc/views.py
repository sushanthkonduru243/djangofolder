import csv
import io
from django.shortcuts import render, redirect
from .models import Customer, Product, Tag, Order
from .forms import OrderForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {'name': 'Raju'})

def add(request):
    try:
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2'])
        val3 = val1 + val2
        return render(request, 'result.html', {'result': val3})
    except (KeyError, ValueError):
        return render(request, 'result.html', {'result': 'Invalid input'})

def createOrder(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'delete.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.success(request, "Password does not follow the rules")
    context = {'form': form}
    return render(request, 'register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.success(request, "Username or Password is incorrect")
        context = {}
        return render(request, 'login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(request, 'dashboard.html', {'customers': customers, 'orders': orders})

def products(request):
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    customers = Customer.objects.all()
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {'customers': customers, 'cust': customer, 'orders': orders, 'ordcount': order_count}
    return render(request, 'customer.html', context)

def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)  # Skip header
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = Customer.objects.update_or_create(
                name=column[0],
                age=column[1],
                date=column[2],
            )
        return redirect('dashboard')
    return render(request, 'import_csv.html')

