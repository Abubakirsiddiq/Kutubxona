from django.db import models

class Muallif(models.Model):
    ism=models.CharField(max_length=30)
    tirik=models.BooleanField()
    yosh=models.PositiveSmallIntegerField()
    kitoblar_soni=models.PositiveSmallIntegerField(blank=True, default=0)
    def __str__(self):
        return self.ism


class Kitob(models.Model):
    a=(
        ("1", "Badiiy"),
        ("2", "Ilmiy"),
        ("3", "Komediya"),
        ("4", "Hujjatli"),
    )
    nom=models.CharField(max_length=30)
    sana=models.DateField(blank=True)
    sahifa=models.PositiveSmallIntegerField()
    janr=models.CharField(max_length=20, choices=a)
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE, related_name="m_kitoblari")
    def __str__(self):
        return self.nom


class Student(models.Model):
    ism=models.CharField(max_length=30)
    guruh=models.PositiveSmallIntegerField(blank=True)
    kitob_soni=models.PositiveSmallIntegerField(default=0)
    bitiruvchi=models.BooleanField()
    def __str__(self):
        return self.ism


class Record(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name="stud")
    kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE, related_name="kito")
    sana=models.DateField(auto_now_add=True)
    def __str__(self):
        return f"{self.kitob}, {self.student}"


