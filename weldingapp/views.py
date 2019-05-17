from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import Order, Item, Orderitem
from . forms import ItemForm, UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView



# Create your views here.
@login_required(login_url= 'weldingapp:login')
def index(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'weldingapp/index2.html', {'orders': orders})

def add_item(request,item_id):
    item = get_object_or_404(Item, id=item_id)
    order_item, ordered = Orderitem.objects.get_or_create(item=item)
    order_q= Order.objects.filter(user=request.user, ordered=False)
    if order_q.exists():
        order = order_q[0]
        if order.items.filter(item__id=item_id).exists():
            order_item.quantity += 1
            order_item.save()
        else :
            order.items.add(order_item)
    else :
        order = Order.objects.create(user=request.user)
        order.items.add(order_item)
    return redirect('weldingapp:index')

def order(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'weldingapp/index.html', context)



def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                orders = Order.objects.filter(user=request.user)
                return render(request, 'weldingapp/index.html', {'orders': orders})
    return render(request, 'weldingapp/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                orders = Order.objects.filter(user=request.user)
                return render(request, 'weldingapp/index2.html', {'orders': orders})
    return render(request, 'weldingapp/login.html')



def logout_user(request):
    logout(request)
    return redirect('weldingapp:login')

def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    orders = Order.objects.filter(user=request.user)
    return render(request, 'weldingapp/index2.html', {'orders': orders})


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    items = order.items.all()
    context = {'order': order,
               'items':items}
    return render(request, 'weldingapp/detail.html', context)



