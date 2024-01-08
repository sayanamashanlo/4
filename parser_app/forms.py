from  django import forms

import parser_app.parser_books
from . import models, parser_books

class ParserForm(forms.Form):
    MEDIA_CHOICES = ("book.ru", 'book.ru')
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'book.ru':
            book_parser = parser_books.book_parser()
            for i in book_parser:
                models.BookModel.create(**i)
