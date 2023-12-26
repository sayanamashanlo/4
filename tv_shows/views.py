from django.shortcuts import render, get_object_or_404
from . import models
from django.shortcuts import render

# Create your views here.


def show_list(request):
    if request.method == 'GET':
        shows = models.Show.objects.all()
        return render(request, template_name='shows/show_list.html',
                      context={'shows': shows})


def show_detail(request, id):
    if request.method == 'GET':
        show_id = get_object_or_404(models.Show, id=id)
        return render(request, template_name='shows/show_detail.html',
                      context={'show_id': show_id})