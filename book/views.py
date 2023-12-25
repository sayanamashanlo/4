from django.shortcuts import render
from . import models
# Create your views here.
def book_view(request):
        if request.method == 'GET':
            book = models.Book.objects.all()
            return render(request, template_name='Library.html',
                          context={'book': book})
