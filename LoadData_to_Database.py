import requests
import json
import psycopg2

r = requests.get('https://jsonplaceholder.typicode.com/users')

print(" Status Code : " , r.status_code)

r.headers['content-type']

r.encoding

r.text

r.json()

data = r.json()

#print(data)
print(type(data))

# for db in data:
#     print(db['id'],'\t',db['name'],'\t',db['username'],'\t',db['email'],'\t',db['website'])

conn = psycopg2.connect(
    dbname='MAHAIT',  #Database
    user='postgres',
    password='postgres',
    host='localhost',
    port='5433'
)

print('Connection is :', conn)

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE raindata (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        website VARCHAR(50) NOT NULL
    )
''')

print('TABLE created successfully')




for db in data:
    cursor.execute(
        'INSERT INTO raindata (id, name, username, email, website) VALUES (%s, %s, %s, %s, %s)',
        (db['id'], db['name'], db['username'],db['email'], db['website'])
    )

print('all data load in database successfully')

conn.commit()
cursor.close()
conn.close()