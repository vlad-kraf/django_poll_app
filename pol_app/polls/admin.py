from django.contrib import admin

# Register your models here.

from . models import Question, Choice

List_of_models = [Question, Choice]

admin.site.register(List_of_models)
