from django.shortcuts import render, get_object_or_404, redirect, reverse
from . models import Order, Item
from . forms import OrderForm, ItemForm, UserForm, Designform
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from welderapp.models import Design



# Create your views here.
@login_required(login_url= 'weldingapp:login')
def index(request):
    orders = Order.objects.filter(user=request.user)

    return render(request, 'weldingapp/index.html', {'orders': orders})


def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'weldingapp/detail.html', {'order': order})

@login_required(login_url= 'weldingapp:login')
def create_order(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        order = form.save(commit=False)
        order.cover = request.FILES['cover']
        order.user = request.user
        order.save()
        return render(request, 'weldingapp/detail.html', {'order': order})
    form = OrderForm()
    return render(request, 'weldingapp/create_order.html', {'form': form})


def create_item(request, order_id):
    form = ItemForm(request.POST or None, request.FILES or None)
    order = get_object_or_404(Order, pk=order_id)
    if form.is_valid():
        item = form.save(commit=False)
        item.client_name = order
        item.design = request.FILES['design']
        item.save()
        context = {'order': order,
               }
        return render(request, 'weldingapp/detail.html', context)

    form = ItemForm()
    return render(request, 'weldingapp/create_item.html', {'form': form})

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
                return render(request, 'weldingapp/index.html', {'orders': orders})
    return render(request, 'weldingapp/login.html')



def logout_user(request):
    logout(request)
    return redirect('weldingapp:login')


def delete_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    orders = Order.objects.all()
    return render(request, 'weldingapp/index.html', {'orders': orders})


def delete_item(request, order_id, item_id):

    order = get_object_or_404(Order, pk=order_id)
    item = get_object_or_404(order.item_set, pk=item_id)
    item.delete()
    context = {'order': order}
    return render(request, 'weldingapp/detail.html', context)


class ItemUpdateView(UpdateView):
        model = Item
        fields = ['item_name', 'length_feet', 'height_feet', 'cost', 'design']

        def get_success_url(self):
            return reverse('weldingapp:index')

        def form_valid(self, form):
            return super().form_valid(form)


@login_required(login_url='weldingapp:login')
def design(request):
    designs =Design.objects.all()
    return render(request, 'weldingapp/index2.html', {'designs': designs})















