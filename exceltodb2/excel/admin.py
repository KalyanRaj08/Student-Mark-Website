from django.contrib import admin
from .models import *

# Register your models here.

class MarksAdmin(admin.ModelAdmin):
    list_display = ('regno', 'name', 'Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16i', 'Q16ii', 'Q17i', 'Q17ii', 'TOTAL','CO1','CO2','CO3','CO4','CO5','CO6','CO7','CO8','CO9','CO10')

admin.site.register(Marks, MarksAdmin)