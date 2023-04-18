# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1o9xJojiIB2Y-sI7mThGVwW5cIHah0OOV
"""

!pip install gpx-converter
!pip install geopandas

import pandas as pd
import geopandas as gpd
from os import listdir
from gpx_converter import Converter
from shapely.geometry import LineString
import numpy as np

# NOTE: data repo in "data"
for filename in listdir("data"):
    if not filename.endswith(".gpx"):
      continue

    gpx_df = Converter(input_file = "data/" + filename).gpx_to_dataframe()
    try:
      gpx_point = gpd.GeoDataFrame(gpx_df, geometry = gpd.points_from_xy(gpx_df.longitude, gpx_df.latitude)).set_crs('epsg:4326')
    except:
      print("WARNING: The file has no record of position, therefore, the matching stopped.")
      continue

    gpx_point['id'] = 1
    try:
      gpx_line = gpx_point.groupby(['id']) ['geometry'].apply(lambda x: LineString(x.tolist()))
    except:
      print("WARNING: The file has only one record of position, therefore, the matching stopped.")
      continue
    
    line_gdf = gpd.GeoDataFrame(gpx_line, geometry = 'geometry').set_crs('epsg:4326')
    latitude = gpx_point["latitude"].iloc[0]
    tolerance_deg = 1 / (111319.488 * np.cos(latitude)) # 1 meter, metric system to degree distance
    line_gdf['geometry'] = line_gdf['geometry'].simplify(tolerance_deg)
    
    geom = line_gdf.iloc[0,0]
    x,y = geom.coords.xy
    coords = pd.DataFrame({'LAT':y,'LON':x})
    new_gpx = Converter.dataframe_to_gpx(coords, lats_colname='LAT', longs_colname='LON', output_file='data/g_' + filename)
    print("New generalised file " + filename + " saved.")