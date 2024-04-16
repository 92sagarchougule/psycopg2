import psycopg2

#Establish Connection of Python to Database

conne = psycopg2.connect(database='GIS', user='postgres', host='localhost', port='5432', password='123')

#Create a Cursor object using cursor() method

cursor = conne.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print("Connection established to: ",data)


#Closing the connection
conne.close()