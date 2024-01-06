from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse


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


def category_list(request):
    if request.method == 'GET':
        categories = models.Category.objects.all()
        return render(request, template_name='shows/categories.html',
                      context={'categories': categories})


def category_show_list(request, category_id):
    category = get_object_or_404(models.Category, id=category_id)
    shows = category.shows.all()
    context = {
        'category': category,
        'shows': shows
    }
    return render(request, template_name='shows/category_shows.html',
                  context=context)


def show_create_view(request):
    if request.method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse(''))
    else:
        form = forms.ShowForm()
        return render(request, template_name='crud/create_show.html',
                      context={'form': form})


def show_list_delete_view(request):
    if request.method == 'GET':
        show_delete = models.Show.objects.all()
        return render(request, template_name='crud/delete/show_list_delete.html',
                      context={'show_delete': show_delete})


def show_drop_view(request, id):
    show_id = get_object_or_404(models.Show, id=id)
    show_id.delete()
    return redirect(reverse('show_list_delete'))


def show_list_edit_view(request):
    if request.method == 'GET':
        show_update = models.Show.objects.all()
        return render(request, template_name='crud/update/show_list_update.html',
                      context={'show_update': show_update})



def show_update(request, id):
    show_id = get_object_or_404(models.Show, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_id, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('show_list_update'))
        else:
            form = form.ShowForm(instance=show_id)
            return render(request, template_name='crud/update/show_update.html',
                          context={
                              "form": form,
                              "show_id": show_id
                          })
