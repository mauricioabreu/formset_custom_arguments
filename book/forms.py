from django import forms

from book import models


class AuthorForm(forms.ModelForm):

    class Meta:
        model = models.Author
        fields = ['name']


class BookForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = ['name', 'isbn', 'author']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(BookForm, self).__init__(*args, **kwargs)
        if user.is_superuser:
            self.fields.update(
                {'price': forms.CharField(label='Price', required=True, widget=forms.NumberInput)}
            )

    def save(self, commit=True):
        book = super(BookForm, self).save(commit=False)
        book.price = self.cleaned_data.get('price', 0)
        book.save()
        return book
