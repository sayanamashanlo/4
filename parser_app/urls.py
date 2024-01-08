from django.urls import  path
from . import views

urlpatterns = [
    path('books_parser', views.ParserBookView.as_view(), name='books_parser')
]