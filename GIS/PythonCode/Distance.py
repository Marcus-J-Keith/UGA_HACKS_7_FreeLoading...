import geopy.distance
import sys
import math
from PyQt5.QtGui import *
import sys
from qgis.core import QgsProject

IncLayerName = "newpoints"
PeopleLayerName = "HelplessPerson"

MapLayers = QgsProject.instance().mapLayersByName(IncLayerName)
PersonLayers = QgsProject.instance().mapLayersByName(PeopleLayerName)
Layer = MapLayers[0]
pLayer = PersonLayers[0]
PlayerArray = []
PlayerArray = [0 for i in range(5)]
for i in range(0, 5) :
    NewPerson = MyStreet(pLayer.getFeature(i), pLayer.getFeature(i).geometry(), pLayer.getFeature(i).geometry().asPoint().y(), pLayer.getFeature(i).geometry().asPoint().x(), pLayer.getFeature(i)['name'])
    PlayerArray[i] = NewPerson
    #print(PlayerArray[i].name)
    
    
array=[]
array = [0 for i in range(65)]
for i in range(0, 65) :
    NewSt = MyStreet(Layer.getFeature(i), Layer.getFeature(i).geometry(), Layer.getFeature(i).geometry().asPoint().y(), Layer.getFeature(i).geometry().asPoint().x(), Layer.getFeature(i)['name'])
    array[i] = NewSt
    #print(array[i].name, array[i].y, array[i].x)



class MyStreet:
    def __init__(self, f, geometry, y, x, name):
        self.f = f
        self.geometry = geometry
        self.y = y
        self.x = x
        self.name = name
        self.Geo = (y,x)
    
print("The closest free parking to", PlayerArray[0].name, "is", array[6].name, "the distance between the two is:",round(geopy.distance.distance(PlayerArray[0].Geo, array[6].Geo).miles,3),"miles")
print("The closest free parking to", PlayerArray[1].name, "is", array[63].name, "the distance between the two is:",round(geopy.distance.distance(PlayerArray[1].Geo, array[63].Geo).miles,3),"miles")
print("The closest free parking to", PlayerArray[2].name, "is", array[56].name, "the distance between the two is:",round(geopy.distance.distance(PlayerArray[2].Geo, array[56].Geo).miles,3),"miles")
print("The closest free parking to", PlayerArray[3].name, "is", array[5].name, "the distance between the two is:",round(geopy.distance.distance(PlayerArray[3].Geo, array[5].Geo).miles,3),"miles")
print("The closest free parking to", PlayerArray[4].name, "is", array[6].name, "the distance between the two is:",round(geopy.distance.distance(PlayerArray[4].Geo, array[6].Geo).miles,3),"miles")
