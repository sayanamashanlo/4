from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, ListView
from . import models, forms, parser_books
# Create your views here.

class ParserBookView(FormView):
    template_name = 'parser.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('Данные взять')
        else:
            return super(ParserBookView).post(request, *args, **kwargs)
