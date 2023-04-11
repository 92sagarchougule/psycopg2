##from sqlalchemy import create_engine
##import geopandas as gpd
## 
##user = "postgres"
##password = "postgres"
##host = "localhost"
##port = 5433
##database = "rainfall"
## 
##conn = f"postgresql://{user}:{password}@{host}:{port}/{database}"
##engine = create_engine(conn)
## 
###Read shapefile using GeoPandas
##gdf = gpd.read_file(r"E:\MahaAgriTech\MRSAC\Data Deployment\Rainfall_Data_SHP\2018\RF_2018.shp")
## 
###Import shapefile to databse
##gdf.to_postgis(name="RF2018", con=engine, schema="public")
## 
##print("success")


import geopandas as gpd
from sqlalchemy import create_engine

# create the sqlalchemy connection engine
db_connection_url = "postgresql://postgres:postgres@localhost:5433/rainfall"
con = create_engine(db_connection_url)

# read in the data
gdf = gpd.read_file(r"E:\MahaAgriTech\MRSAC\Data Deployment\Rainfall_Data_SHP\2018\RF_2018.shp")

print(gdf)

# Drop nulls in the geometry column
print('Dropping ' + str(gdf.geometry.isna().sum()) + ' nulls.')
gdf = gdf.dropna(subset=['geometry'])

# Push the geodataframe to postgresql
gdf.to_postgis("redlining", con, index=False, if_exists='replace')

print('done Successfully')
