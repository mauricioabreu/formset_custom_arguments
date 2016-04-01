from django.contrib import admin

from book import models


class BookInline(admin.StackedInline):
    model = models.Book
    extra = 0


class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


admin.site.register(models.Author, AuthorAdmin)
