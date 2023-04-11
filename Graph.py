import pandas
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

engine = create_engine("postgresql:///?User=postgres&;Password=postgres&Database=MAHAIT&Server=20.219.135.232/&Port=5432")

print(engine)

df = pandas.read_sql("SELECT gid, dist_code  FROM district", engine)

df.plot(kind="bar", x="dist_code", y="gid")

plt.show()
