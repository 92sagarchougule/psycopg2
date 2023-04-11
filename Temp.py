import psycopg2

conn = psycopg2.connect(
    dbname='MIT',  #Database
    user='postgres',
    password='postgres',
    host='20.219.135.232',
    port='5432'
)

print(" database connected successfully", conn)

cur = conn.cursor()

#cur.execute("SELECT COUNT (DISTINCT NAME) from COMPANY")

cur.execute(""" SELECT * FROM district 
            WHERE dist_name like '%k%' """)


rows = cur.fetchall()

#print(rows)


for row in rows:
    print(row[0], '\t',row[1],'\t', row[2])