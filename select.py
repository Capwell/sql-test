import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.execute('''


''')


for result in cur:
    print(result)

con.commit()
con.close()
