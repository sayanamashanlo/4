from django.urls import path
from . import views

urlpatterns = [
    path('show_list/', views.show_list, name='show_list'),
    path('show_list/<int:id>/', views.show_detail, name='show_detail'),
    path('category_list/', views.category_list, name='category'),
    path('categories/<int:category_id>/', views.category_show_list, name='category_shows'),
]