# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:18:45 2020

@author: HASSAN ENTERPRISES
"""

import folium
m=folium.Map(location=[54.525963,-105.255119],tiles="Stamen Toner",zoom_start=16)
m
#=================================================================================================================
folium.Marker(location=[54.525963,-105.255119],popup="seattle",tooltip="click for more information").add_to(m)
m
#==================================================================================================================
folium.Marker(location=[54.525963,-105.255119],popup="<strong>seattle</strong>",tooltip="click for more information").add_to(m)
m
#=====================================================================================================
folium.Marker(location=[54.525963,-105.255119],popup="<strong>seattle</strong>",tooltip="click for more information",icon=folium.Icon(icon="cloud")).add_to(m)
m
#==================================================================================================
folium.Marker(location=[54.525963,-105.255119],popup="<strong>seattle</strong>",tooltip="click for more information",icon=folium.Icon(icon="envelope",color="red")).add_to(m)
m
#====================================================================================================
m = folium.Map(location=[45.523, -122.675],width=750, height=500)
m = folium.Map(location=[45.523, -122.675],
                           tiles='stamen Toner')
m = folium.Map(location=(45.523, -122.675), max_zoom=20,
                           tiles='Cloud')
m = folium.Map(location=[45.523, -122.675],zoom_start=2,tiles='Stamen Toner',attr='Mapbox attribution')
m

#===================================== tiles attributes ==========================================
#“OpenStreetMap”
#“Mapbox Bright” (Limited levels of zoom for free tiles)
#“Mapbox Control Room” (Limited levels of zoom for free tiles)
#“Stamen” (Terrain, Toner, and Watercolor)
#“Cloudmade” (Must pass API key)
#“Mapbox” (Must pass API key)
#“CartoDB” (positron and dark_matter)

locationspiderman=[40.728291,-73.844612]
#justifying an latitude and longitute
iconspiderman=folium.features.CustomIcon("spiderman.jpg",icon_size=(100,100))
popupspiderman="<strong>spiderman</strong><br>Realname:peterparkeer<br>cityof birth:Forest hill queens,Ny,USA"
folium.Marker(location=locationspiderman,popup=popupspiderman,icon=iconspiderman).add_to(m)
m


