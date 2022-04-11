import sqlite3

conn = sqlite3.connect('lunch.db') #connect to database
c = conn.cursor() # access to the database


# make columns and data type


# c.execute('''DROP TABLE meals''') ## delete table from database

c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')
sandwich = 'jam'
fruit = 'sandwich'
tablenum = 23

c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))

conn.commit() # after insert don't forget to commit

c.execute('''SELECT * FROM meals''')
# c.execute('''SELECT fruit FROM meals''')
results = c.fetchall()
print(results)