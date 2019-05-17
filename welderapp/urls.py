from django.urls import path

from . import views
from .views import DesignUpdateView, ItemUpdateView

app_name = 'welderapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<demand_id>[0-9]+)/', views.details, name='details'),
    path('create_order', views.create_order, name='create_order'),
    path('(?P<demand_id>[0-9]+)/delete_demand', views.delete_demand, name='delete_demand'),
    path('(?P<demand_id>[0-9]+)/create_design', views.create_design, name='create_design'),
    path('(?P<demand_id>[0-9]+)/delete_design(?P<design_id>[0-9]+)/', views.delete_design, name='delete_design'),
    path('<int:pk>/update/', DesignUpdateView.as_view(), name='update'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_item', views.add_item, name='add_item'),
    path('items', views.items, name='items'),
    path('<int:pk>/update_item/', ItemUpdateView.as_view(), name='update_item'),
    path('(?P<item_id>[0-9]+)/delete_item', views.delete_item, name='delete_item'),
    path('orders', views.orders, name='orders'),
    path('(?P<order_id>[0-9]+)/detail', views.detail, name='detail'),

]
