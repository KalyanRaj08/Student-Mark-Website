import sqlite3
import csv
import io

db =sqlite3.connect('Marks.sqlite',check_same_thread=False)
dbh = db.cursor()

dbh.executescript('''
DROP TABLE IF EXISTS marks;
CREATE TABLE IF NOT EXISTS marks(
    sno INTEGER PRIMARY KEY AUTOINCREMENT,
    regno INTEGER,
    name TEXT NOT NULL,
    Q1 REAL,
    Q2 REAL,
    Q3 REAL,
    Q4 REAL, 
    Q5 REAL,
    Q6 REAL,
    Q7 REAL,
    Q8 REAL,
    Q9 REAL,
    Q10 REAL,
    Q11 REAL,
    Q12 REAL,
    Q13 REAL,
    Q14 REAL,
    Q15 REAL,
    Q16i REAL, 
    Q16ii REAL,
    Q17i REAL,
    Q17ii REAL,
    TOTAL REAL,
    CO1 REAL,
    CO2 REAL,
    CO3 REAL,
    CO4 REAL,
    CO5 REAL,
    CO6 REAL,
    CO7 REAL,
    CO8 REAL,
    CO9 REAL,
    CO10 REAL);
''')

def handle_uploaded_filedbms(f):
    marks = f
    print(marks)
    for i in marks:
        dbh.execute('INSERT INTO marks(regno,name,Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15,Q16i,Q16ii,'
                    'Q17i,Q17ii,TOTAL,CO1,CO2,CO3,CO4,CO5,CO6,CO7,CO8,CO9,CO10) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',(i.regno,i.name,i.Q1,i.Q2,i.Q3,i.Q4,i.Q5,i.Q6,i.Q7,i.Q8,i.Q9,i.Q10,i.Q11,i.Q12,i.Q13,i.Q14,i.Q15,i.Q16i,i.Q16ii,i.Q17i,i.Q17ii,i.TOTAL,i.CO1,i.CO2,i.CO3,i.CO4,i.CO5,i.CO6,i.CO7,i.CO8,i.CO9,i.CO10))
        db.commit()

def printdbms():
    dbh.execute('SELECT * FROM marks')
    check = dbh.fetchall()
    for i in check:
        print(i)