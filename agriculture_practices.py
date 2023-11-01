import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
# import main as m

survey_data = pd.read_excel("survey_data.xlsx", sheet_name=None)
location = pd.read_excel("provinces&district.xlsx", )


def showData(district,s):

    col1,col2,col3,col4 = stl.columns(4)
    
    new_column_names = ['District','Overall','SSF','LSF']
    seasonal_practices = survey_data.get('Table 55')
    districts = seasonal_practices['District'].drop(0)

    cols = seasonal_practices.columns

    if str(districts).strip().__contains__(district):
        stl.text(f"Precentage of farmers by agricultural practices  in Season A 2022, {district,s} district")

        with col1:
            protected_land = seasonal_practices[cols[0:4]]
            protected_land.set_axis(new_column_names,axis=1, inplace=True)
            protected_land = protected_land.drop(0)
            protected_land_by_district = protected_land[protected_land['District']==district]
            # drawing figue
            data = [protected_land_by_district['SSF'].sum(),protected_land_by_district['LSF'].sum()]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(textposition='inside',hoverinfo='percent+label')
            fig.update_layout(width=250, height=250)
            stl.plotly_chart(fig,use_container_width=True)

        with col2:
            machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
            machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
            machinary_equipments.set_axis(new_column_names,axis=1, inplace=True)
            machinary_equipments_by_district = machinary_equipments[machinary_equipments['District'] == district]
            # drawing figue
            data = [machinary_equipments_by_district['SSF'].sum(),machinary_equipments_by_district['LSF'].sum()]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(textposition='inside',hoverinfo='percent+label')
            fig.update_layout(width=250, height=250)
            stl.plotly_chart(fig,use_container_width=True)

        with col3:
            irrigation = seasonal_practices[cols[7:10]].drop(0)
            irrigation = pd.concat([districts,irrigation], axis=1)
            irrigation.set_axis(new_column_names,axis=1, inplace=True)
            irrigation_by_district = irrigation[irrigation['District'] == district]
            # drawing figue
            data = [irrigation_by_district['SSF'].sum(),irrigation_by_district['LSF'].sum()]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(textposition='inside',hoverinfo='percent+label')
            fig.update_layout(width=250, height=250,annotations=[dict(text='GHG', x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)   
                     
        with col4:
            agroforestry = seasonal_practices[cols[10:]].drop(0)
            agroforestry = pd.concat([districts,agroforestry], axis=1)
            agroforestry.set_axis(new_column_names,axis=1, inplace=True)
            agroforestry_by_district = agroforestry[agroforestry['District'] == district]
            # drawing figue
            data = [agroforestry_by_district['SSF'].sum(),agroforestry_by_district['LSF'].sum()]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(textposition='inside',hoverinfo='percent+label')
            fig.update_layout(width=250, height=250)
            stl.plotly_chart(fig,use_container_width=True)             
    else:
        stl.text('Precentage of farmers by agricultural practices  in Season A 2022')

        with col1:
            protected_land = seasonal_practices[cols[0:4]]
            protected_land.set_axis(new_column_names,axis=1, inplace=True)
            protected_land = protected_land.drop(0)
            ## drawing figue
            data = [protected_land['SSF'][31],protected_land['LSF'][31]]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(textposition='inside',hoverinfo='percent+label')
            fig.update_layout(width=250, height=250,annotations=[dict(text='GHG', x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

            with col2:
                machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
                machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
                machinary_equipments.set_axis(new_column_names,axis=1, inplace=True)
                 ## drawing figue
                data = [machinary_equipments['SSF'][31],machinary_equipments['LSF'][31]]
                Lables = ['SSF','LSF']
                fig = px.pie(data, values=data, names=Lables, hole=0.5)
                fig.update_traces(textposition='inside',hoverinfo='percent+label')
                fig.update_layout(width=250, height=250)
                stl.plotly_chart(fig,use_container_width=True)

            with col3:
                irrigation = seasonal_practices[cols[7:10]].drop(0)
                irrigation = pd.concat([districts,irrigation], axis=1)
                irrigation.set_axis(new_column_names,axis=1, inplace=True)
                ## drawing figue
                data = [irrigation['SSF'][31],irrigation['LSF'][31]]
                Lables = ['SSF','LSF']
                fig = px.pie(data, values=data, names=Lables, hole=0.5)
                fig.update_traces(textposition='inside',hoverinfo='percent+label')
                fig.update_layout(width=250, height=250)
                stl.plotly_chart(fig,use_container_width=True)
                
            with col4:
                agroforestry = seasonal_practices[cols[10:]].drop(0)
                agroforestry = pd.concat([districts,agroforestry], axis=1)
                agroforestry.set_axis(new_column_names,axis=1, inplace=True)
                ## drawing figue
                data = [agroforestry['SSF'][31],agroforestry['LSF'][31]]
                Lables = ['SSF','LSF']
                fig = px.pie(data, values=data, names=Lables, hole=0.5)
                fig.update_traces(textposition='inside',hoverinfo='percent+label')
                fig.update_layout(width=250, height=250)
                stl.plotly_chart(fig,use_container_width=True)
                    
                    