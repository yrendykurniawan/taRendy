import sqlite3

conn = sqlite3.connect('../dataset/nrc/asli/sinonim/translate/anger.db')
c = conn.cursor()
for row in c.execute('SELECT data_komen FROM dataku'):
    print(row[0])