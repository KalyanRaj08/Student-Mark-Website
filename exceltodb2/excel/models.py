from django.db import models
from django import forms

# Create your models here.

class ExcelandCO(models.Model):
    no = models.IntegerField()
    co1 = models.CharField(max_length=100)
    co2 = models.CharField(max_length=100)
    co3 = models.CharField(max_length=100)
    co4 = models.CharField(max_length=100)
    co5 = models.CharField(max_length=100)
    co6 = models.CharField(max_length=100)
    co7 = models.CharField(max_length=100)
    co8 = models.CharField(max_length=100)
    co9 = models.CharField(max_length=100)
    co10 = models.CharField(max_length=100)
    file = models.FileField()

class Marks(models.Model):
    regno = models.IntegerField()
    name = models.CharField(max_length = 100)
    Q1 = models.CharField(max_length = 3)
    Q2 = models.CharField(max_length = 3)
    Q3 = models.CharField(max_length = 3)
    Q4 = models.CharField(max_length = 3)
    Q5 = models.CharField(max_length = 3)
    Q6 = models.CharField(max_length = 3)
    Q7 = models.CharField(max_length = 3)
    Q8 = models.CharField(max_length = 3)
    Q9 = models.CharField(max_length = 3)
    Q10 = models.CharField(max_length = 3)
    Q11 = models.CharField(max_length = 3)
    Q12 = models.CharField(max_length = 3)
    Q13 = models.CharField(max_length = 3)
    Q14 = models.CharField(max_length = 3)
    Q15 = models.CharField(max_length = 3)
    Q16i = models.CharField(max_length = 3)
    Q16ii = models.CharField(max_length = 3)
    Q17i = models.CharField(max_length = 3)
    Q17ii = models.CharField(max_length = 3)
    TOTAL = models.CharField(max_length = 3)
    CO1 = models.CharField(max_length = 3)
    CO2 = models.CharField(max_length=3)
    CO3 = models.CharField(max_length=3)
    CO4 = models.CharField(max_length=3)
    CO5 = models.CharField(max_length=3)
    CO6 = models.CharField(max_length=3)
    CO7 = models.CharField(max_length=3)
    CO8 = models.CharField(max_length=3)
    CO9 = models.CharField(max_length=3)
    CO10 = models.CharField(max_length=3)

class ExcelandCOForm(forms.ModelForm):
    class Meta():
        model = ExcelandCO
        exclude =()

class MarksForm(forms.ModelForm):
    class Meta():
        model = Marks
        exclude = ()