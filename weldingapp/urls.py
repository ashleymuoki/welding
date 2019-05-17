from django.urls import path
from . import views

app_name = 'weldingapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<order_id>[0-9]+)/', views.detail, name='detail'),
    path('order/', views.order, name='order'),
    path('(?P<item_id>[0-9]+)/add_item/', views.add_item, name='add_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('(?P<order_id>[0-9]+)/delete_order', views.delete_order, name='delete_order'),





]
