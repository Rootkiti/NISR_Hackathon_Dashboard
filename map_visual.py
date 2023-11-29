import pandas as pd
import numpy as np
import streamlit as stl
import folium


@stl.cache_data
def draw_map(area_land,agri_land):
    cordinater = pd.read_excel('districts_with_lat&long.xlsx')
    def make_data():
        pass

    CONNECTICUT_CENTER = (-1.964663,30.064436)


    map = folium.Map(location=CONNECTICUT_CENTER, zoom_start=8.5)
    for i in range(0, 30):
        location =[cordinater['latitude'][i],cordinater['longitude'][i]]
        folium.Marker(location,popup = (f'District: {cordinater["district"][i]}\n Total Area: {area_land[i]}Ha\n Agriculture Land: {agri_land[i]}Ha'),tooltip=cordinater["district"][i]).add_to(map)
        
    
    return map