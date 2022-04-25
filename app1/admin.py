from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    fields = ("nom", "sahifa", "janr", "sana", "muallif")
    list_display = ("nom", "muallif", "janr")
    search_fields = ("id", "nom", "sahifa")
    list_filter = ("janr",)
    autocomplete_fields = ("muallif",)


@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ("id", "ism", "tirik")

admin.site.register(Student)
admin.site.register(Record)
