from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def salomlash(request):
    return HttpResponse("Salom Dunyo")

def malumot(request):
    return HttpResponse("Assalomualaykum men Nabiyev Abubakirsiddiq")

def Loyiha(request):
    return  HttpResponse("Biz kutubxona tizimini quryabmiz")

def asosiy(request):
    return render(request, "asosiy.html")

def salomlash(request):
    return render(request, "salomlash.html")

def malumot(request):
    return render(request, "malumot.html")

def loyiha(request):
    hammasi=Kitob.objects.all()
    return render(request, "loyiha.html", {"kitoblar":hammasi})


# Vazifa 2-qism

# 1
def katta_muallif(request):
    ham=Muallif.objects.filter(yosh__gte=45)
    return render(request, "Katta_muallif.html", {"muallif": ham})

# 2
def hammasi_record(request):
    hammasi=Record.objects.all()
    return render(request, "Hammasi_record.html", {"record": hammasi})

# 3
def ilmiy(request):
    il=Kitob.objects.filter(janr="non-fiction")
    return render(request, "Ilmiy.html", {"Ilmi": il})

# 4
def muallif1(request):
    mual=Muallif.objects.all()
    return render(request, "Muallif2.html", {"m": mual})


# Dars

def mualliflar(request):
    m=Muallif.objects.all().order_by("ism")
    return render(request, "Muallif.html", {"avtorlar": m})

# vazifa

def student(request):
    if request.method =='POST':
        if request.POST.get("t") == "False":
            natija = False
        else:
            natija = True
        Student.objects.create(
            ism=request.POST.get("ismi"),
            guruh=request.POST.get("g"),
            bitiruvchi=natija,
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/student/")
    soz=request.GET.get("qidirish")
    if soz == None:
        birga=Student.objects.all().order_by("ism")
    else:
        birga=Student.objects.filter(ism=soz)
    return render(request, "Student.html", {"student": birga})


def student_ochir(request, son):
    Student.objects.get(id=son).delete()
    return redirect("/student/")


def muallif(request):
    if request.method =='POST':
        if request.POST.get("t") == "False":
            natija = False
        else:
            natija = True
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            tirik=natija,
            yosh=request.POST.get("y"),
            kitoblar_soni=request.POST.get("k_s")
        )
        return redirect("/muallif/")
    soz=request.GET.get("qidirish")
    if soz == None:
        birga=Muallif.objects.all().order_by("ism")
    else:
        birga=Muallif.objects.filter(ism=soz)
    return render(request, "muallif3.html", {"muallif": birga})


def muallif_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/muallif/")


def record_ochir(request, son):
    Record.objects.get(id=son).delete()
    return redirect("/record/")

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/kitob/")
# Dars


def kitoblar(request):
    if request.method =='POST':
        m = request.POST.get("m")
        muallif=Muallif.objects.get(id=m)
        Kitob.objects.create(
            nom=request.POST.get("nom"),
            sana=request.POST.get("sana"),
            sahifa=request.POST.get("sahifa"),
            janr=request.POST.get("janr"),
            muallif=muallif,
        )
        return redirect("/kitob/")
    soz=request.GET.get("qidirish")
    m=Muallif.objects.all()
    if soz == None:
        hammasi=Kitob.objects.all().order_by("nom")
    else:
        hammasi=Kitob.objects.filter(nom=soz)
    return render(request, "Kitob.html", {"kitoblar":hammasi, "avtorlar":m})


def record(request):
    if request.method == 'POST':
        s = request.POST.get("s")
        k = request.POST.get("k")
        student = Student.objects.get(id=s)
        kitob = Kitob.objects.get(id=k)
        Record.objects.create(
            student=student,
            kitob=kitob,
        )
        return redirect("/record/")
    s=Student.objects.all()
    k=Kitob.objects.all()
    soz = request.GET.get("qidirish")
    if soz == None:
        birga = Record.objects.all().order_by("sana")
    else:
        birga = Record.objects.filter(sana=soz)
    return render(request, "Record.html", {"record": birga, "studentlar":s})


# Dars


def kitob_edit(request, a):
    if request.method =="POST":
        k1=Kitob.objects.get(id=a)
        k1.nom=request.POST.get("nom")
        k1.sahifa=request.POST.get("sahifa")
        k1.janr=request.POST.get("janr")
        mu=Muallif.objects.get(id=request.POST.get("muallif"))
        k1.muallif=mu
        k1.save()
        return redirect("/kitob/")
    k=Kitob.objects.get(id=a)
    m=Muallif.objects.all()
    return render(request, "kitob_edit.html", {"kitob":k, "muallif":m})

# def student_edit(request, a):
#     if request.method =="POST":
#         s1=Student.objects.get(id=a)
#         s1.ism=request.POST.get("ism")
#         s1.guruh=request.POST.get("guruh")
#         s1.kitob_soni=request.POST.get("kitob_s")
#         s1.=request.POST.get("kitob_s")


