import psycopg2

conn = psycopg2.connect(database="MAHAIT",
                        host="localhost",
                        user="postgres",
                        password="postgres",
                        port="5433")

print(conn)
cursor = conn.cursor()

cursor.execute("SELECT * FROM rf_2018 WHERE gid = 1")

rows = cursor.fetchall()



for row in rows:
    #print('\n',row[0],'\n',row[1],'\n',row[2],'\n',row[3],'\n',row[4],'\n',row[5],'\n',row[6])
    print("ID = ", row[0])
    print("Circle Code = ", row[1])
    print("Circle = ", row[2])
    print("District = ", row[3], "\n")
    #print("District = ", row[4])
