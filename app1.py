# Data geojson diambil melalui geojson.io 

# Import libraries
import folium
from folium import plugins

import ipywidgets
import os
import json

# latitude and Longitude pusat (Kolam intel/titik pusat itb ganesha)
Pusat = (-6.890375765348438,107.61037727860213)

# Fungsi mengganti latitude dan longitude 
def switchPosition(coordinate):
  temp = coordinate[0]
  coordinate[0] = coordinate[1]
  coordinate[1] = temp
  return coordinate

# Position Selector
selectPosition_widget=ipywidgets.Select(
    options=['Gerbang SR', 'Gerbang Belakang', 'Gerbang Sipil'],
    value='Gerbang Belakang',
    description='Pilih Gerbang',
    disabled=False)
def selectPosition(position):
    global tanda
    if position == 'Gerbang SR':
        tanda = 'e'
        selectGedung_widget=ipywidgets.Select(
        options=['BSC B',
         'Gedung Kimia',
         'GKU T',
         'LabTek 1',
         ],
        value='GKU T',
        description='Gedung Tujuan',
        disabled=False)
    if position == 'Gerbang Belakang':
        tanda = 'n'
        selectGedung_widget=ipywidgets.Select(
        options=['BSC B',
         'Lab Fisika Dasar',
         'Gedung Kimia',
         'GKU B',
         'GKU T',
         'Oktagon',
         'LabTek 1',
         'TVST'],
        value='Gedung Kimia',
        description='Gedung Tujuan',
        disabled=False)
    if position == 'Gerbang Sipil':
        tanda = 'w'
        selectGedung_widget=ipywidgets.Select(
        options=['GKU B',
         'Oktagon',
         'TVST'],
        value='GKU B',
        description='Gedung Tujuan',
        disabled=False)
    ipywidgets.interact(selectGedung, way=selectGedung_widget)  

#Initialization   
ipywidgets.interact(selectPosition, position=selectPosition_widget)

# widget function
def selectGedung(way):
    global gedungOutline
    global rute
    global tanda
    print(way)
    if way == 'BSC B':
        gedungOutline = 'DataKampus/gedung1.geojson'
        if tanda == 'e':
            rute = 'DataKampus/rute/e21.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n1.geojson'
    if way == 'Lab Fisika Dasar':
        gedungOutline = 'DataKampus/gedung2.geojson'
        if tanda == 'n':
            rute = 'DataKampus/rute/n2.geojson'
    if way == 'Gedung Kimia':
        gedungOutline = 'DataKampus/gedung3.geojson'
        if tanda == 'e':
            rute = 'DataKampus/rute/e23.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n3.geojson'
    if way == 'GKU B':
        gedungOutline = 'DataKampus/gedung4.geojson'
        if tanda == 'w':
            rute = 'DataKampus/rute/w14.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n4.geojson'
    if way == 'GKU T':
        gedungOutline = 'DataKampus/gedung5.geojson'
        if tanda == 'e':
            rute = 'DataKampus/rute/e25.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n5.geojson'
    if way == 'Oktagon':
        gedungOutline = 'DataKampus/gedung6.geojson'
        if tanda == 'w':
            rute = 'DataKampus/rute/w16.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n6.geojson'
    if way == 'LabTek 1':
        gedungOutline = 'DataKampus/gedung7.geojson'
        if tanda == 'e':
            rute = 'DataKampus/rute/e27.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n7.geojson'
    if way == 'TVST':
        gedungOutline = 'DataKampus/gedung8.geojson'
        if tanda == 'w':
            rute = 'DataKampus/rute/w18.geojson'
        elif tanda == 'n':
            rute = 'DataKampus/rute/n8.geojson'
    # Fungsi dari lib folium, inisialiasi peta 
    peta_kampus = folium.Map(location = Pusat, width = "60%", height = "95%", zoom_start = 16) 
    # Menampilkan outline dari gedung (sesuai dengan data geojson yang telah diambil sebelumnya)
    display(folium.GeoJson(gedungOutline, zoom_on_click=True).add_to(peta_kampus))
    # Dengan membuka var rute (yaitu directory file) 
    with open(rute) as f:
      Rute = json.load(f)

    for feature in Rute['features']:
        path = feature['geometry']['coordinates']
    finalRute = list(map(switchPosition,path))
    # finalRute
    folium.plugins.AntPath(finalRute).add_to(peta_kampus)
    display(peta_kampus)
