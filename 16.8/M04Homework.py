import csv
import pandas as pd
import sqlite3 as sq
import sqlalchemy as sa


# with open('books','rt') as fin:
#     cin = csv.DictReader(fin, fieldnames=['author', 'book'])
#     books = [row for row in cin]

conn = sq.connect('books.db')
curs = conn.cursor()
curs.execute("create table if not exists books" +
             " (title text,author text, year integer)")

books = pd.read_csv('books2.csv')
books.to_sql('books', connection, if_exists='replace', index=False)
curs.execute('select * from books')

curs.execute('SELECT title FROM books ORDER BY ASC')
records = curs.fetchall()
for row in records:
    print(row)
curs.close()
conn.close()