# formset_custom_arguments
An example of how to use formset custom arguments for Django <= 1.8

This repository contains an example of how to pass custom argumentos to formsets using Django <= 1.8

It is already [built-in in Django 1.9](https://docs.djangoproject.com/en/1.9/topics/forms/formsets/#passing-custom-parameters-to-formset-forms)

## About the example

A Django app called `book` where you can authors and theirs books.
Only superusers can add the price of the books.  The problem here is that it is not easy to pass any arguments to the forms of a formset.
