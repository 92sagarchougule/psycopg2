import geopandas as gpd
import psycopg2
from sqlalchemy import create_engine

# Set your PostgreSQL connection parameters
db_connection = {
    'host': 'localhost',
    'dbname': 'learn_post',
    'user': 'postgres',
    'password': '123',
    'port': '5432'
}

# Path to your shapefile
shapefile_path = 'C:\\Users\\sagar.chougule\\Desktop\\cropsap\\CROPSAP_SEP_2023.shp'

# Read the shapefile using geopandas
gdf = gpd.read_file(shapefile_path)

# Create a connection to PostgreSQL
conn_str = "postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}".format(**db_connection)
engine = create_engine(conn_str)

# Insert the GeoDataFrame into PostgreSQL
gdf.to_postgis(name='crop', con=engine, if_exists='replace', index=False)
