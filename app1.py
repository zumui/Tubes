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



class navigator:
    def __init__(self):
        self.DataKampus = {}
        self.kampusLocation =(-6.890375765348438,107.61037727860213)
        self.position = 'n'
        self.destination = 'gedung4'

        for root, dirs, files in os.walk('DataKampus'):  
            for file in files:
                self.DataKampus[file.split('.')[0]] = root+'/'+file

    def changeDestination(self,newDestination):
        self.destination = newDestination
        self.redrawMap()

    def changeStartPoint(self, newStartPoint):
        
        #self.position = newStartPoint #does not work yet
        print(f'Selected Start: {newStartPoint}; Selected Target: {self.destination}')
        #self.redrawMap()
        

    def drawPathWay(self,kampusMap):
      # Fungsi mengganti latitude dan longitude
      def switchPosition(coordinate):
        temp = coordinate[0]
        coordinate[0] = coordinate[1]
        coordinate[1] = temp
        return coordinate

      searchString = self.position + self.destination.split('gedung')[1]
      with open(self.DataKampus[searchString]) as f:
           contohRute = json.load(f)

      for feature in contohRute['features']:
        path = feature['geometry']['coordinates']

      finalPath = list(map(switchPosition,path))
      folium.plugins.AntPath(finalPath).add_to(kampusMap)

    def drawBuilding(self,kampusMap):
      gedungOutline = self.DataKampus[self.destination]
      folium.GeoJson(Outline, name="geojson").add_to(kampusMap)

    def redrawMap(self):
        #print(f'position {self.position}, destination {self.destination}')
        kampusMap = folium.Map(location = self.kampusLocation, width = "75%", zoom_start = 17)
        self.drawPathWay(kampusMap)
        self.drawBuilding(kampusMap)
        display(kampusMap)

myNavigator = navigator()

def displayWay(whereTo):
     myNavigator.changeDestination(whereTo)
def changePosition(whereFrom):
    myNavigator.changeStartPoint(whereFrom)

selectGedung_widget=ipywidgets.Select(
options=['BSC B',
         'Lab Fisika Dasar',
         'Gedung Kimia',
         'GKU B',
         'GKU T',
         'Oktagon',
         'LabTek 1',
         'TVST'],
    value='BSC B',
    description='Target',
    disabled=False)
# widget function
def selectGedung(way):
    if way == 'BSC B' :
        displayWay('gedung1' ) 
    if way == 'Lab Fisika Dasar':
        displayWay('gedung2')
    if way == 'Gedung Kimia':
        displayWay('gedung3')
    if way == 'GKU B':
        displayWay('gedung4')
    if way == 'GKU T':
        displayWay('gedung5')
    if way == 'Oktagon':
        displayWay('gedung6')
    if way == 'LabTek 1':
        displayWay('gedung7')
    if way == 'TVST':
        displayWay('gedung8')

# Position Selector
selectPosition_widget=ipywidgets.Select(
    options=['Gerbang SR', 'Gerbang Belakang', 'Gerbang Sipil'],
    value='Gerbang Belakang',
    description='Start',
    disabled=False)

def selectPosition(position):
    if position == 'Gerbang SR':
        changePosition('e')
    if position == 'Gerbang Belakang':
        changePosition('n')
    if position == 'Gerbang sipil':
        changePosition('w')
        
#Initialization   
ipywidgets.interact(selectPosition, position=selectPosition_widget)
ipywidgets.interact(selectGedung, way=selectGedung_widget)
