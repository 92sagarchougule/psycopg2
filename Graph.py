import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5433/MAHAIT')
print('Engine Joined to Postgres ')
print(engine)
df = pandas.read_sql("SELECT id, salary  FROM company", engine)
df.plot(kind="line", x="id", y="salary", color='blue', title='Rainfall',label="Rainfall", style='-*')
#plt.figure(figsize=(10, 10))


plt.savefig(r'E:/rainfall.png')
plt.show()
