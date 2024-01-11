from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views import View
from . import models, forms


class AllClothList(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/cloth_list.html'

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class ClothListMale(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/male_cloth.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для мужчин')


class ClothListFemale(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/female_cloth.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для женщин')


class ClothListKids(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/kids_cloth.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='для детей')


class ClothListUni(generic.ListView):
    model = models.ProductCl
    template_name = 'clothes/uni_cloth.html'

    def queryset(self):
        return self.model.objects.filter(tags__name='универсальный')


class CreateOrderView(View):
    template_name = 'clothes/create_order.html'
    form_class = forms.OrderForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form})


    # тег
    # { %for tag in i.tags.all %}
     # {{tag.name}}</h2>