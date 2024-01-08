from django.urls import path
from . import views

app_name = 'shows'
urlpatterns = [
    path('', views.ShowlistView.as_view(), name='show_list'),
    path('show_list/<int:id>/', views.ShowDetailView.as_view(), name='show_detail'),

    path('category_list/', views.category_list, name='category'),
    path('categories/<int:category_id>/', views.category_show_list, name='category_shows'),

    path('create_show/', views.ShowCreateView.as_view(), name='show_create'),

    path('show_list_delete/', views.show_list_delete_view, name='show_list_delete'),

    path('show_drop/<int:id>/delete/', views.ShowDropView.as_view(), name='show_drop'),

    path('show_list_update/', views.show_list_edit_view, name='show_list_update'),

    path('show_update/<int:id>/update/', views.ShowUpdateView.as_view(), name='show_update'),
    path('search/', views.SearchView.as_view(), name='search')
]
