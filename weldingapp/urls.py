from django.urls import path
from . import views
from . views import ItemUpdateView
from welderapp.views import design

app_name = 'weldingapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<order_id>[0-9]+)/', views.detail, name='detail'),
    path('create_order', views.create_order, name='create_order'),
    path('(?P<order_id>[0-9]+)/create_item', views.create_item, name='create_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('(?P<order_id>[0-9]+)/delete_order', views.delete_order, name='delete_order'),
    path('(?P<order_id>[0-9]+)/delete_item(?P<item_id>[0-9]+)/', views.delete_item, name='delete_item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('design', views.design, name='design'),





]
