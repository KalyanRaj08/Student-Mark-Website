import sqlite3
import csv
import io

lq = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16(i)','16(ii)','17(i)','17(ii)']
lm = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,15,15,15,15]

def handle_uploaded_filecsv(f):
    marks = []
    print(f)
    H = 'Register Number,Name,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16(i),Q16(ii),Q17(i),Q17(ii),TOTAL,CO1,CO2,CO3,CO4,CO5,CO6,CO7,CO8,CO9,CO10'
    b = H.split(',')
    marks.append(b)
    for i in f:
        b = [i.regno,i.name,i.Q1,i.Q2,i.Q3,i.Q4,i.Q5,i.Q6,i.Q7,i.Q8,i.Q9,i.Q10,i.Q11,i.Q12,i.Q13,i.Q14,i.Q15,i.Q16i,i.Q16ii,i.Q17i,i.Q17ii,i.TOTAL,i.CO1,i.CO2,i.CO3,i.CO4,i.CO5,i.CO6,i.CO7,i.CO8,i.CO9,i.CO10]
        marks.append(b)
    with open('Marks.csv',"w",newline="\n") as file:
        writer = csv.writer(file)
        writer.writerows(marks)