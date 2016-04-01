from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.functional import curry

from book import forms, models


def add_new_author(request):
    BookFormset = inlineformset_factory(
        models.Author,
        models.Book,
        form=forms.BookForm,
        extra=1,
        can_delete=False,
    )
    BookFormset.form = staticmethod(
        curry(
            forms.BookForm,
            user=request.user
        )
    )
    form = forms.AuthorForm()
    books_formset = BookFormset()
    if request.method == 'POST':
        form = forms.AuthorForm(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            books_formset = BookFormset(request.POST, instance=author)
            if books_formset.is_valid():
                author.save()
                books_formset.save()
                return HttpResponseRedirect(reverse('new_author'))
    return render_to_response(
        'add_new_author.html',
        {'form': form, 'formset': books_formset},
        RequestContext(request)
    )
