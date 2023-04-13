import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@172.25.0.8:5432/MIT')
print('Engine Joined to Postgres ')
print(engine)
df = pandas.read_sql("SELECT tahname, august  FROM cs_2022_ndvi", engine)

# if(df["august"] == 'None'):
#     print(df["august"])

for db in len(df["august"]):
    print(df)

# df.plot(kind="bar", x=df["august"], y="tahname", color='blue', title='Rainfall',label="Rainfall")


# plt.show()