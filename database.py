import sqlite3

conn = sqlite3.connect('jobs.db') #connect to database
c = conn.cursor() # access to the database


# make columns and data type


# c.execute('''DROP TABLE jobs''') ## delete table from database

# c.execute('''CREATE TABLE jobs(Title TEXT, Company TEXT, Location TEXT, Date TEXT, Summary TEXT)''')
title = 'swe'
company = 'sap'
location = 'vancouver'
date = '1 day ago'
summary = 'yadayadayada'

c.execute('''INSERT INTO jobs VALUES(?,?,?,?,?)''', (title, company, location, date, summary))

# conn.commit() # after insert don't forget to commit

c.execute('''SELECT * FROM jobs''')
# c.execute('''SELECT Title FROM jobs''')
results = c.fetchall()
print(results)