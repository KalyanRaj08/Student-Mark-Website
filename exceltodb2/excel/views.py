from django.shortcuts import render
from django.http import *
from django.template import loader
from .models import *
from .writedbms import *
from .writecsv import *
from django.contrib import messages
import io

# Create your views here.

def home(request):
    t = loader.get_template('home.html')
    return render(request,'home.html')

def input(request):
    t = loader.get_template('input.html')
    return render(request, 'input.html', {'forms': ExcelandCOForm})

def acceptfile(request):
    flag = 0
    lq = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16(i)', '16(ii)', '17(i)', '17(ii)']
    lm = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 7.5, 7.5, 7.5, 7.5]
    if request.method == 'POST':
        f = request.FILES['file']
        n = int(request.POST['no'])
        cos = []
        cos.append(request.POST['co1'].split(','))
        cos.append(request.POST['co2'].split(','))
        cos.append(request.POST['co3'].split(','))
        cos.append(request.POST['co4'].split(','))
        cos.append(request.POST['co5'].split(','))
        cos.append(request.POST['co6'].split(','))
        cos.append(request.POST['co7'].split(','))
        cos.append(request.POST['co8'].split(','))
        cos.append(request.POST['co9'].split(','))
        cos.append(request.POST['co10'].split(','))
        convs = 15 / n
        marks = []
        file = f.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        for row in reader:
            marks.append(row)
        for i in marks:
            form = MarksForm()
            sum = 0.0
            l = list(i.values())
            for j in range(3, 22):
                if l[j] != '':
                    sum = sum + float(l[j])
            cosv = []
            post = form.save(commit=False)
            post.regno = i['Register Number']
            post.name = i['Name']
            post.Q1 = i['Q1']
            post.Q2 = i['Q2']
            post.Q3 = i['Q3']
            post.Q4 = i['Q4']
            post.Q5 = i['Q5']
            post.Q6 = i['Q6']
            post.Q7 = i['Q7']
            post.Q8 = i['Q8']
            post.Q9 = i['Q9']
            post.Q10 = i['Q10']
            post.Q11 = i['Q11']
            post.Q12 = i['Q12']
            post.Q13 = i['Q13']
            post.Q14 = i['Q14']
            post.Q15 = i['Q15']
            post.Q16i = i['Q16(i)']
            post.Q16ii = i['Q16(ii)']
            post.Q17i = i['Q17(i)']
            post.Q17ii = i['Q17(ii)']
            post.TOTAL = sum
            he =  [i['Q1'],i['Q2'],i['Q3'],i['Q4'],i['Q5'],i['Q6'],i['Q7'],i['Q8'],i['Q9'],i['Q10'],i['Q11'],i['Q12'],i['Q13'],i['Q14'],i['Q15'],i['Q16(i)'],i['Q16(ii)'],i['Q17(i)'],i['Q17(ii)'] ]
            for j in range(n):
                tots = 0.0
                totsy = 0.0
                for k in range(15):
                    if lq[k] in cos[j]:
                        if he[k] != '':
                            tots = tots + float(he[k])
                        totsy = totsy + lm[k]
                for k in range(15,19):
                    if lq[k] in cos[j]:
                        if k % 2 == 1 :
                            if he[k] == '' and he[k+1] != '':
                                continue
                            elif he[k] != '' and he[k+1] == '':
                                tots = tots + float(he[k])
                                totsy = totsy + 15
                            elif he[k] == '' and he[k+1] == '':
                                totsy = totsy +15
                        else :
                            if he[k] == '' and he[k-1] != '':
                                continue
                            elif he[k] != '' and he[k-1] == '':
                                tots = tots + float(he[k])
                                totsy = totsy + 15
                k = tots/totsy * convs
                cosv.append(k)
            for j in range(n,10):
                cosv.append('')
            post.CO1 = cosv[0]
            post.CO2 = cosv[1]
            post.CO3 = cosv[2]
            post.CO4 = cosv[3]
            post.CO5 = cosv[4]
            post.CO6 = cosv[5]
            post.CO7 = cosv[6]
            post.CO8 = cosv[7]
            post.CO9 = cosv[8]
            post.CO10 = cosv[9]
            try:
                post.save()
            except:
                flag = 1

        if flag == 0:
            messages.info(request, 'SUCCESSFULLY UPLOADED FILE!')
            return HttpResponseRedirect('/input/')
        else:
            messages.info(request, 'SORRY COULD NOT UPLOAD FILE! NOTE:SOME ROWS MIGHT BEEN UPLOADED!')
            return HttpResponseRedirect('/input/')

def home2(request):
    t = loader.get_template('home2.html')
    return render(request, 'home2.html')

def save1(request):
    try:
        mark = Marks.objects.all()
        handle_uploaded_filecsv(mark)
        t = loader.get_template('save.html')
        return render(request, 'save.html')
    except:
        t = loader.get_template('save2.html')
        return render(request, 'save2.html')

def save2(request):
    try:
        mark = Marks.objects.all()
        handle_uploaded_filedbms(mark)
        t = loader.get_template('save.html')
        return render(request, 'save.html')
    except:
        t = loader.get_template('save2.html')
        return render(request, 'save2.html')

def delete(request):
    try:
        Marks.objects.all().delete()
        t = loader.get_template('delete1.html')
        return render(request, 'delete1.html')
    except:
        t = loader.get_template('delete2.html')
        return render(request, 'delete2.html')