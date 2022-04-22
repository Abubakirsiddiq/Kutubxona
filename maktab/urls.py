
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom', salomlash),
    path('men/', malumot),
    path('loyiha/', loyiha),
    path('asosiy/', asosiy),
    path('student/', student),
    path("katta_muallif/", katta_muallif),
    path("mualliflar/", mualliflar),
    path('student/<int:son>/', student_ochir),
    path("record/", record),
    path("ilmiy/", ilmiy),
    path("muallif/", muallif),
    path('muallif/<int:son>/', muallif_ochir),
    path('record/<int:son>/', record_ochir),
    path('kitob/', kitoblar),
    path('kitob_edit/<int:a>/', kitob_edit),
    path('kitob/<int:son>/', kitob_ochir),
]
