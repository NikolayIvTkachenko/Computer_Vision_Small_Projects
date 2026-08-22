# cartopy
# pip install cartopy

import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

calif_cities = us_cities[us_cities.State.eq('California')]

fig, ax = plt.subplots(figsize=(15, 8))

ax = plt.axes(projection=ccrs.Mercator())
ax.coastlines('10m')
ax.set_yticks([32, 33, 34, 35, 36], crs=ccrs.PlateCarree()) #30, 31,
ax.set_xticks([-121, -120, -119, -118, -117, -116, -115], crs=ccrs.PlateCarree())

lon_formatter = LongitudeFormatter()
lat_formatter = LatitudeFormatter()

ax.xaxis.set_major_formatter(lon_formatter)
ax.yaxis.set_major_formatter(lat_formatter)

ax.set_extent([-121, -115, 32, 36])

X = calif_cities['lon']
Y = calif_cities['lat']

ax.scatter(X, Y, color='red', marker='o', transform=ccrs.PlateCarree())

plt.show()


