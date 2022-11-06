import folium
from folium import plugins
import pandas as pd

import ipywidgets
import os
import json

# the latitude and Longitude coordinates (Kolam intel/titik pusat itb ganesha)
Pusat = (-6.890375765348438,107.61037727860213)
# Fungsi dari lib folium, inisialiasi peta 
peta_kampus = folium.Map(location = Pusat, width = "60%", height = "95%", zoom_start = 16) 
# peta_kampus dipanggil
peta_kampus

# Menampilkan outline dari gedung (sesuai dengan data geojson yang telah diambil sebelumnya)
gedungOutline = 'DataKampus/gedung5.geojson'
display(folium.GeoJson(gedungOutline, name="GKU T", zoom_on_click=True).add_to(peta_kampus))
# display(peta_kampus)

contohGeoJson = 'DataKampus/rute/e25.geojson'

# Fungsi mengganti latitude dan longitude 
def switchPosition(coordinate):
  temp = coordinate[0]
  coordinate[0] = coordinate[1]
  coordinate[1] = temp
  return coordinate

# Dengan membuka var contohGeoJson (yaitu directory file) 
with open(contohGeoJson) as f:
  contohRute = json.load(f)

for feature in contohRute['features']:
    path = feature['geometry']['coordinates']
finalRute = list(map(switchPosition,path))
finalRute

rute = 'DataKampus/rute/e25.geojson'
folium.plugins.AntPath([[-6.893498102792378, 107.61184596608075],
 [-6.892505158606696, 107.61184263216938],
 [-6.892399244437513, 107.6119159782209],
 [-6.892184106208589, 107.611925979955],
 [-6.892067864663304, 107.61203505879286],
 [-6.891948908251763, 107.61221272624641],
 [-6.8914402667078605, 107.61222098984877],
 [-6.891343357916966, 107.61221463819061],
 [-6.8910011945586405, 107.6121356551684],
 [-6.890761182070335, 107.61210348150422],
 [-6.890533242741142, 107.61211748136537]]
).add_to(peta_kampus)
peta_kampus