import psycopg2

#Establish Connection of Python to Database

conne = psycopg2.connect(database='GIS', user='postgres', host='localhost', port='5432', password='123')

#Create a Cursor object using cursor() method

conne.autocommit = True

cursor = conne.cursor()


# sql = """ CREATE Table Employee(
#             First_Name CHAR(25),
#             Last_Name CHAR(25),
#             Age int,
#             Income FLOAT,
#             Sex CHAR(10)
#             )"""


# sql = """ INSERT INTO Employee(First_Name, Last_Name, Age, Income, Sex)
#             VALUES('MahaIT','Orgnization',15, 215487965,'M')"""


# cursor.execute(sql)

# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#  INCOME) VALUES ('Ramya', 'Rama priya', 27, 'F', 9000)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#  INCOME) VALUES ('Vinay', 'Battacharya', 20, 'M', 6000)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#  INCOME) VALUES ('Sharukh', 'Sheik', 25, 'M', 8300)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#  INCOME) VALUES ('Sarmista', 'Sharma', 26, 'F', 10000)''')
# cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
#  INCOME) VALUES ('Tripthi', 'Mishra', 24, 'F', 6000)''')

sql = """ SELECT * FROM Employee"""

cursor.execute(sql)

result = cursor.fetchall()

print(result)


print('Created Database Sucssefully')


#Closing the connection
conne.close()