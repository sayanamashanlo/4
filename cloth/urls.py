from django.urls import path
from . import views

urlpatterns = [
    path('all_cloth/', views.AllClothList.as_view()),
    path('male_cloth/', views.ClothListMale.as_view(), name='male_cloth'),
    path('female_cloth/', views.ClothListFemale.as_view(), name='female_cloth'),
    path('kids_cloth/', views.ClothListKids.as_view(), name='kids_cloth'),
    path('uni_cloth/', views.ClothListUni.as_view(), name='uni_cloth'),
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    # path('cloth_list/', views.ClothList.as_view(), name='cloth_list'),
]