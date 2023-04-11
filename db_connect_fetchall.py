#!/usr/bin/python

import psycopg2


conn = psycopg2.connect(database="MAHAIT", user = "postgres", password = "postgres", host = "localhost", port = "5433")



print("Opened database successfully")


cur = conn.cursor()

#cur.execute("SELECT COUNT (DISTINCT NAME) from COMPANY")

cur.execute("SELECT * from raindata")


rows = cur.fetchall()

#print(rows)


for row in rows:
    print(row[0],'     \t     ',row[1],'     \t      ',row[2], '      \t     ',row[3])
    # print(row[2])
##   print("ID = ", row[0])
##   print("NAME = ", row[1])
##   print("ADDRESS = ", row[2])
##   print("SALARY = ", row[3], "\n")

print("Operation done successfully")


conn.close()
