import sqlite3
import os
import csv
from datetime import datetime

now = datetime.now() # current date and time
date_time = now.strftime("%m_%d_%Y__%H")

connection = sqlite3.connect('database.db')


#with open('schema.sql') as f:
#    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("SELECT * FROM posts")

rows = cur.fetchall()

for row in rows:
        print(row)

#Get the date as string

# name of csv file 
filename_base = "Exer_baklog_"
filename_extension = ".csv"

filename_full = filename_base + str(date_time) + filename_extension
    
# writing to csv file 
with open(filename_full, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
    

connection.close()