from django.urls import path

from . import views
from weldingapp.views import ItemUpdateView


app_name = 'welderapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('(?P<order_id>[0-9]+)/', views.detail, name='detail'),
    path('create_order', views.create_order, name='create_order'),
    path('(?P<order_id>[0-9]+)/create_item', views.create_item, name='create_item'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='update'),
    path('(?P<order_id>[0-9]+)/delete_order', views.delete_order, name='delete_order'),
    path('(?P<order_id>[0-9]+)/delete_item(?P<item_id>[0-9]+)/', views.delete_item, name='delete_item'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create_design', views.create_design, name='create_design'),
    path('design/', views.design, name='design'),

]
