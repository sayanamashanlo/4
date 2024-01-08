from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic


# Create your views here.
# Create all in classes
# generic - это готовые классы


class ShowlistView(generic.ListView):
    template_name = 'shows/show_list.html'
    model = models.Show

    def get_queryset(self):
        return self.model.objects.all()


# def show_list(request):
#     if request.method == 'GET':
#         shows = models.Show.objects.all()
#         return render(request, template_name='shows/show_list.html',
#                       context={'shows': shows})


class ShowDetailView(generic.DetailView):
    template_name = 'shows/show_detail.html'
    context_object_name = 'show_id'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)


# def show_detail(request, id):
#     if request.method == 'GET':
#         show_id = get_object_or_404(models.Show, id=id)
#         return render(request, template_name='shows/show_detail.html',
#                       context={'show_id': show_id})


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


# логика для создания поста
class ShowCreateView(generic.CreateView):
    template_name = 'crud/create_show.html'
    model = models.Show
    form_class = forms.ShowForm
    success_url = 'shows:create_show'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowCreateView, self).form_valid(form=form)


# def show_create_view(request):
#     if request.method == 'POST':
#         form = forms.ShowForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse(''))
#     else:
#         form = forms.ShowForm()
#         return render(request, template_name='crud/create_show.html',
#                       context={'form': form})

# логика для удаления чего либо
def show_list_delete_view(request):
    if request.method == 'GET':
        show_delete = models.Show.objects.all()
        return render(request, template_name='crud/delete/show_list_delete.html',
                      context={'show_delete': show_delete})


class ShowDropView(generic.DeleteView):
    template_name = 'crud/delete/confirm_delete.html'
    success_url = 'show_list_delete'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)


# def show_drop_view(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#     show_id.delete()
#     return redirect(reverse('show_list_delete'))

# добавление
def show_list_edit_view(request):
    if request.method == 'GET':
        show_update = models.Show.objects.all()
        return render(request, template_name='crud/update/show_list_update.html',
                      context={'show_update': show_update})


class ShowUpdateView(generic.UpdateView):
    template_name = 'crud/update/show_update.html'
    form_class = forms.ShowForm
    success_url = 'show_list_update'

    def get_object(self, **kwargs):
        show_id = self.kwargs.get('id')
        return get_object_or_404(models.Show, id=show_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ShowUpdateView, self).form_valid(form=form)


# def show_update(request, id):
#     show_id = get_object_or_404(models.Show, id=id)
#     if request.method == 'POST':
#         form = forms.ShowForm(instance=show_id, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('show_list_update'))
#         else:
#             form = form.ShowForm(instance=show_id)
#             return render(request, template_name='crud/update/show_update.html',
#                           context={
#                               "form": form,
#                               "show_id": show_id
#                           })

# search
# технический английский
#     paginate_by = --- список страниц(количесво)
# name__icontains --- это поле для обькта по поиску
# q - query

class SearchView(generic.ListView):
    template_name =  'shows/show_list.html'
    paginate_by = 3

    def get_queryset(self):
        return models.Show.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
            context = super(SearchView, self).get_context_data(**kwargs)
            context['q'] = self.request.GET.get('q')
            return context