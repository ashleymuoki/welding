from django.shortcuts import render, get_object_or_404, redirect, reverse
from . forms import OrderForm, UserForm,DesignForm, ItemForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,CreateView
from .models import Design, Demand
from weldingapp.models import Item , Order , Orderitem



@login_required(login_url= 'welderapp:login')
def index(request):
    demands = Demand.objects.filter(user=request.user)
    context = {'demands': demands}
    return render(request, 'welderapp/index.html', context)


def details(request, demand_id):
    demand = get_object_or_404(Demand, pk=demand_id)
    context = {'demand': demand}
    return render(request, 'welderapp/detail.html', context)

@login_required(login_url= 'welderapp:login')
def create_order(request):
    form = OrderForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        demand = form.save(commit=False)
        demand.cover = request.FILES['cover']
        demand.user = request.user
        demand.save()
        return render(request, 'welderapp/detail.html', {'demand': demand})
    form = OrderForm()
    return render(request, 'welderapp/create_order.html', {'form': form})


def create_design(request, demand_id):
    form = DesignForm(request.POST or None, request.FILES or None)
    demand = get_object_or_404(Demand, pk=demand_id)
    if form.is_valid():
        design = form.save(commit=False)
        design.name = demand
        design.design = request.FILES['design']
        design.save()
        context = {'demand': demand,
               }
        return render(request, 'welderapp/detail.html', context)

    form = DesignForm()
    return render(request, 'welderapp/create_design.html', {'form': form})

def delete_design(request, demand_id, design_id):
    demand = get_object_or_404(Demand, pk=demand_id)
    design = get_object_or_404(demand.design_set, pk=design_id)
    design.delete()
    context = {'demand': demand}
    return render(request, 'welderapp/detail.html', context)


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
                orders = Demand.objects.filter(user=request.user)
                return render(request, 'welderapp/index.html', {'orders': orders})
    return render(request, 'welderapp/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                orders = Demand.objects.filter(user=request.user)
                return render(request, 'welderapp/index.html', {'orders': orders})
    return render(request, 'welderapp/login.html')



def logout_user(request):
    logout(request)
    return redirect('welderapp:login')


class DesignUpdateView(UpdateView):
        model = Design
        fields = ['item', 'length_feet', 'height_feet', 'cost', 'design']

        def get_success_url(self):
            return reverse('welderapp:index')

        def form_valid(self, form):
            return super().form_valid(form)

def delete_demand(request, demand_id):
    demand = Demand.objects.get(pk=demand_id)
    demand.delete()
    demands = Demand.objects.filter(user=request.user)
    return render(request, 'welderapp/index.html', {'demands': demands})



@login_required(login_url= 'welderapp:login')
def add_item(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        item = form.save(commit=False)
        item.cover = request.FILES['design']
        item.user = request.user
        item.save()
        items = Item.objects.filter(user=request.user)
        return render(request, 'welderapp/index2.html', {'items': items})
    form = ItemForm()
    return render(request, 'welderapp/create_item.html', {'form': form})


@login_required(login_url= 'welderapp:login')
def items(request):
    items = Item.objects.all()
    context = {'items': items}

    return render(request, 'welderapp/index2.html', context)

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['item', 'length_feet', 'height_feet', 'cost', 'design']

    def get_success_url(self):
        return reverse('welderapp:index')

    def form_valid(self, form):
        return super().form_valid(form)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.delete()
    items = Item.objects.filter(user=request.user)
    return render(request, 'welderapp/index2.html', {'items':items})



@login_required(login_url= 'welderapp:login')
def orders(request):
    orders = Order.objects.all()
    return render(request, 'welderapp/index3.html', {'orders': orders})

def detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    context = {'order': order}
    return render(request, 'welderapp/details.html', context)

