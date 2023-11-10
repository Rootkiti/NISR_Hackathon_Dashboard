import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
import plotly.graph_objects as go
# import main as m

survey_data = pd.read_excel("survey_data.xlsx", sheet_name=None)
location = pd.read_excel("provinces&district.xlsx", )


def showData(district,s):
    stl.subheader('Agriculture Practices By Farmer Categories Per Season And District In 2022 (%)')               
    x = ['Season A','Season B','Season C']
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
            data = [round(protected_land_by_district['SSF'].sum(),1),round(protected_land_by_district['LSF'].sum(),1)]
            notation = round(protected_land_by_district['Overall'].sum(),1)
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Land protection (%)",width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col2:
            machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
            machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
            machinary_equipments.set_axis(new_column_names,axis=1, inplace=True)
            machinary_equipments_by_district = machinary_equipments[machinary_equipments['District'] == district]
            # drawing figue
            data = [round(machinary_equipments_by_district['SSF'].sum(),1),round(machinary_equipments_by_district['LSF'].sum(),1)]
            notation = round(machinary_equipments_by_district['Overall'].sum(),1)
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Use Of Machinary (%)",width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col3:
            irrigation = seasonal_practices[cols[7:10]].drop(0)
            irrigation = pd.concat([districts,irrigation], axis=1)
            irrigation.set_axis(new_column_names,axis=1, inplace=True)
            irrigation_by_district = irrigation[irrigation['District'] == district]
            # drawing figue
            data = [round(irrigation_by_district['SSF'].sum(),1),round(irrigation_by_district['LSF'].sum(),1)]
            notation = round(irrigation_by_district['Overall'].sum(),1)
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Irrigation (%)",width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)  
                     
        with col4:
            agroforestry = seasonal_practices[cols[10:]].drop(0)
            agroforestry = pd.concat([districts,agroforestry], axis=1)
            agroforestry.set_axis(new_column_names,axis=1, inplace=True)
            agroforestry_by_district = agroforestry[agroforestry['District'] == district]
            # drawing figue
            data = [round(agroforestry_by_district['SSF'].sum(),1),round(agroforestry_by_district['LSF'].sum(),1)]
            notation = round(agroforestry_by_district['Overall'].sum(),1)
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Agroforestry (%)",width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)            
    else:
        stl.text('Precentage of farmers by agricultural practices  in Season A 2022')

        with col1:
            protected_land = seasonal_practices[cols[0:4]]
            protected_land.set_axis(new_column_names,axis=1, inplace=True)
            protected_land = protected_land.drop(0)
            ## drawing figue
            data = [round(protected_land['SSF'][31],1),round(protected_land['LSF'][31],1)]
            notation = protected_land['Overall'][31]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Land protection (%)",width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col2:
            machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
            machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
            machinary_equipments.set_axis(new_column_names,axis=1, inplace=True)
                ## drawing figue
            data = [round(machinary_equipments['SSF'][31],1),round(machinary_equipments['LSF'][31],1)]
            notation = machinary_equipments['Overall'][31]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(title_text="Use Of Machinary (%)",width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col3:
            irrigation = seasonal_practices[cols[7:10]].drop(0)
            irrigation = pd.concat([districts,irrigation], axis=1)
            irrigation.set_axis(new_column_names,axis=1, inplace=True)
            ## drawing figue
            data = [round(irrigation['SSF'][31],1),round(irrigation['LSF'][31],1)]
            notation = irrigation['Overall'][31]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')

            fig.update_layout(title_text="Irrigation (%)",width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)
            
        with col4:
            agroforestry = seasonal_practices[cols[10:]].drop(0)
            agroforestry = pd.concat([districts,agroforestry], axis=1)
            agroforestry.set_axis(new_column_names,axis=1, inplace=True)
            ## drawing figue
            data = [round(agroforestry['SSF'][31],1),round(agroforestry['LSF'][31],1)]
            notation = agroforestry['Overall'][31]
            Lables = ['SSF','LSF']
            fig = px.pie(data, values=data, names=Lables, hole=0.5)
            fig.update_traces(hoverinfo='percent+label', textinfo='none')

            fig.update_layout(title_text="Agroforestry (%)",width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)
    if(district == ''):
        stl.subheader('  (%) Use Of Modern Irrigation Methods Per Season In 2022') 
    elif (district =='choose your option'):
        stl.subheader('  (%) Use Of Modern Irrigation Methods Per Season In 2022') 
    else:
        stl.subheader(f'(%) Use Of Modern Irrigation Methods Per Season In {district} District 2022')               
              

    # stl.subheader('  (%) Use Of Modern Irrigation Methods Per Season In 2022')               
 #  types of irrigation section
    type1,type2,type3,type4,type5= stl.columns(5)
    irrigation_type = survey_data.get("Table 58")
    irrigation_type.drop(0)
    clrs = ['#B0BF1A','#045F5F','#FFFACD']
    cols = irrigation_type.columns
    if str(districts).strip().__contains__(district):
        value = district
        with type1:            
            # surface irrigation
            Surface_irrigation = irrigation_type[cols[:4]]
            n_cols = ['District','Season A','Season B','Season C']
            Surface_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Surface_irrigation = Surface_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Surface_irrigation = Surface_irrigation.fillna(0)
            district_Surface_irrigation = Surface_irrigation[Surface_irrigation['District'] == district]
            district_Surface_irrigation = round(district_Surface_irrigation,1)
            y = [district_Surface_irrigation['Season A'].sum(),district_Surface_irrigation['Season B'].sum(),district_Surface_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Surface Irrigation', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type2:
            # flood irrigation
            Flood_irrigation = irrigation_type[cols[4:7]]
            Flood_irrigation = pd.concat([irrigation_type['District'].drop(0),Flood_irrigation],axis=1)
            Flood_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Flood_irrigation = Flood_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Flood_irrigation = Flood_irrigation.fillna(0)
            Flood_irrigation = round(Flood_irrigation,1)
            district_Flood_irrigation = Flood_irrigation[Flood_irrigation['District']==district]
            y = [district_Flood_irrigation['Season A'].sum(),district_Flood_irrigation['Season B'].sum(),district_Flood_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Flood Irrigation', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type3:
            # Drip irrigation
            Drip_irrigation = irrigation_type[cols[7:10]]
            Drip_irrigation = pd.concat([irrigation_type['District'].drop(0),Drip_irrigation],axis=1)
            Drip_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Drip_irrigation = Drip_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Drip_irrigation = Drip_irrigation.fillna(0)
            Drip_irrigation = round(Drip_irrigation,1)
            district_Drip_irrigation = Drip_irrigation[Drip_irrigation['District'] == district]
            y = [district_Drip_irrigation['Season A'].sum(),district_Drip_irrigation['Season B'].sum(),district_Drip_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Drip Irrigation', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type4:

            # Sprinkler irrigation
            Sprinkle_irrigation = irrigation_type[cols[10:13]]
            Sprinkle_irrigation = pd.concat([irrigation_type['District'].drop(0),Sprinkle_irrigation],axis=1)
            Sprinkle_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Sprinkle_irrigation = Sprinkle_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Sprinkle_irrigation = Sprinkle_irrigation.fillna(0)
            Sprinkle_irrigation = round(Sprinkle_irrigation,1)
            district_Sprinkle_irrigation = Sprinkle_irrigation[Sprinkle_irrigation['District'] == district]
            
            y = [district_Sprinkle_irrigation['Season A'].sum(),district_Sprinkle_irrigation['Season B'].sum(),district_Sprinkle_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Sprinkler Irrigation', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type5:
            # Pivot irrigation
            Pivot_irrigation = irrigation_type[cols[13:16]]
            Pivot_irrigation = pd.concat([irrigation_type['District'].drop(0),Pivot_irrigation],axis=1)
            Pivot_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Pivot_irrigation = Pivot_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Pivot_irrigation = Pivot_irrigation.fillna(0)
            Pivot_irrigation = round(Pivot_irrigation,1)
            district_Pivot_irrigation = Pivot_irrigation[Pivot_irrigation['District'] == district]
            
            y = [district_Pivot_irrigation['Season A'].sum(),district_Pivot_irrigation['Season B'].sum(),district_Pivot_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Pivot Irrigation', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
      
    else:
        with type1:
            # surface irrigation
            Surface_irrigation = irrigation_type[cols[:4]]
            n_cols = ['District','Season A','Season B','Season C']
            Surface_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Surface_irrigation = Surface_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Surface_irrigation = Surface_irrigation.fillna(0)
            Surface_irrigation = round(Surface_irrigation,1)
            y = [Surface_irrigation['Season A'][30],Surface_irrigation['Season B'][30],Surface_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Surface Irrigation'), font_color='red',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

        with type2:            
            # flood irrigation
            Flood_irrigation = irrigation_type[cols[4:7]]
            Flood_irrigation = pd.concat([irrigation_type['District'].drop(0),Flood_irrigation],axis=1)
            Flood_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Flood_irrigation = Flood_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Flood_irrigation = Flood_irrigation.fillna(0)
            Flood_irrigation = round(Flood_irrigation,1)
            y = [Flood_irrigation['Season A'][30],Flood_irrigation['Season B'][30],Flood_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Flood Irrigation'), font_color='red',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type3:
            # Drip irrigation
            Drip_irrigation = irrigation_type[cols[7:10]]
            Drip_irrigation = pd.concat([irrigation_type['District'].drop(0),Drip_irrigation],axis=1)
            Drip_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Drip_irrigation = Drip_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Drip_irrigation = Drip_irrigation.fillna(0)
            Drip_irrigation = round(Drip_irrigation,1)
            y = [Drip_irrigation['Season A'][30],Drip_irrigation['Season B'][30],Drip_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Flood Irrigation'), font_color='red',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type4:

            # Sprinkler irrigation
            Sprinkle_irrigation = irrigation_type[cols[10:13]]
            Sprinkle_irrigation = pd.concat([irrigation_type['District'].drop(0),Sprinkle_irrigation],axis=1)
            Sprinkle_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Sprinkle_irrigation = Sprinkle_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Sprinkle_irrigation = Sprinkle_irrigation.fillna(0)
            Sprinkle_irrigation = round(Sprinkle_irrigation,1)
            y = [Sprinkle_irrigation['Season A'][30],Sprinkle_irrigation['Season B'][30],Sprinkle_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Sprinkler Irrigation'), font_color='red',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type5:
            # Pivot irrigation
            Pivot_irrigation = irrigation_type[cols[13:16]]
            Pivot_irrigation = pd.concat([irrigation_type['District'].drop(0),Pivot_irrigation],axis=1)
            Pivot_irrigation.set_axis(n_cols,axis=1,inplace=True)
            Pivot_irrigation = Pivot_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Pivot_irrigation = Pivot_irrigation.fillna(0)
            Pivot_irrigation = round(Pivot_irrigation,1)
            y = [Pivot_irrigation['Season A'][30],Pivot_irrigation['Season B'][30],Pivot_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Pivot Irrigation'), font_color='red',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
    if(district == ''):
       stl.subheader('  Source Of Water Used In Irrigation Per Season In 2022 (%)')  
    elif (district =='choose your option'):
       stl.subheader('  Source Of Water Used In Irrigation Per Season In 2022 (%)')  
    else:
        stl.subheader(f'Source Of Water Used In Irrigation Per Season In {district} District 2022 (%)')  

    
   #  source of water used in irrigation activities
    source1,source2,source3,source4,source5 = stl.columns(5)
    water_source = survey_data.get('Table 59')
    cols = water_source.columns
    districts = water_source[cols[0]]
    column_names = ['District',	'Season A',	'Season B',	'Season C']
    colors = ['#254117','#1F6357','#3EA99F']
    

    if str(districts).strip().__contains__(district):
        
        with source1:
            # 1. Rain water
            rainwater = water_source[cols[:4]]
            rainwater = rainwater.drop(0)
            rainwater.set_axis(column_names, axis=1, inplace=True)
            rainwater = rainwater.fillna(0)
            rainwater = round(rainwater,1)
            rainwater_per_district = rainwater[rainwater['District'] == district]
            y = [rainwater_per_district['Season A'].sum(),rainwater_per_district['Season B'].sum(),rainwater_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Rain Water'), font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

            
        with source2:
            
            water_treatment = pd.concat([districts,water_source[cols[4:7]]], axis=1)
            water_treatment = water_treatment.drop(0)
            water_treatment.set_axis(column_names, axis=1, inplace=True)
            water_treatment = water_treatment.fillna(0)
            water_treatment = round(water_treatment,1)
            water_treatment_per_district = water_treatment[water_treatment['District'] == district]
            y = [water_treatment_per_district['Season A'].sum(),water_treatment_per_district['Season B'].sum(),water_treatment_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f' Water treatment', font_color='red',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
            ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source3:
            # 3. underground water
            underground_water = pd.concat([districts,water_source[cols[7:10]]], axis=1)
            underground_water = underground_water.drop(0)
            underground_water.set_axis(column_names, axis=1, inplace=True)
            underground_water = underground_water.fillna(0)
            underground_water = round(underground_water,1)
            underground_water_per_district = underground_water[underground_water['District'] == district]
            y = [underground_water_per_district['Season A'].sum(),underground_water_per_district['Season B'].sum(),underground_water_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=f'Underground Water', font_color='red',titlefont_size=13,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
              ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source4:
            # 4. lake/stream water
            lake_or_stream_water = pd.concat([districts,water_source[cols[10:13]]], axis=1)
            lake_or_stream_water = lake_or_stream_water.drop(0)
            lake_or_stream_water.set_axis(column_names, axis=1, inplace=True)
            lake_or_stream_water = lake_or_stream_water.fillna(0)
            lake_or_stream_water = round(lake_or_stream_water,1)
            lake_or_stream_water_perdistrict = lake_or_stream_water[lake_or_stream_water['District'] == district]
            y = [lake_or_stream_water_perdistrict['Season A'].sum(),lake_or_stream_water_perdistrict['Season B'].sum(),lake_or_stream_water_perdistrict['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=f'Lake / streams Water', font_color='red',titlefont_size=13,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
               ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source5:
           # 5. water catchment 
           water_catchment = pd.concat([districts,water_source[cols[13:]]], axis=1)
           water_catchment = water_catchment.drop(0)
           water_catchment.set_axis(column_names, axis=1, inplace=True)
           water_catchment = water_catchment.fillna(0)
           water_catchment = round(water_catchment,1)
           water_catchment_per_district = water_catchment[water_catchment['District'] == district]
           y = [water_catchment_per_district['Season A'].sum(),water_catchment_per_district['Season B'].sum(),water_catchment_per_district['Season C'].sum()]
           fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
           textposition='outside')])

           fig.update_layout(title_text=f'Water catchment', font_color='red',titlefont_size=15,  yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                     ),)
           stl.plotly_chart(fig, use_container_width=True)

    else:
        with source1:
            
            # 1. Rain water
            rainwater = water_source[cols[:4]]
            rainwater = rainwater.drop(0)
            rainwater.set_axis(column_names, axis=1, inplace=True)
            rainwater = rainwater.fillna(0)
            rainwater = round(rainwater,1)
            y = [rainwater['Season A'][31],rainwater['Season B'][31],rainwater['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y], 
            textposition='outside')])

            fig.update_layout(title_text=('Rain Water'), titlefont_size=15,titlefont_color='green',title_x = 0.3,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                                
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
            
        with source2:
            # 2. water treatment
            water_treatment = pd.concat([districts,water_source[cols[4:7]]], axis=1)
            water_treatment = water_treatment.drop(0)
            water_treatment.set_axis(column_names, axis=1, inplace=True)
            water_treatment = water_treatment.fillna(0)
            water_treatment = round(water_treatment,1)
            y = [water_treatment['Season A'][31],water_treatment['Season B'][31],water_treatment['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Water Treatment'), font_color='red',titlefont_size=15,titlefont_color='green',title_x = 0.2,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ))
            stl.plotly_chart(fig, use_container_width=True)

        with source3:            # 3. underground water
            underground_water = pd.concat([districts,water_source[cols[7:10]]], axis=1)
            underground_water = underground_water.drop(0)
            underground_water.set_axis(column_names, axis=1, inplace=True)
            underground_water = underground_water.fillna(0)
            underground_water = round(underground_water,1)
            y = [underground_water['Season A'][31],underground_water['Season B'][31],underground_water['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'underground Water'), font_color='red',titlefont_size=15,titlefont_color='green',title_x = 0.1,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source4:
            # 4. lake/stream water
            lake_or_stream_water = pd.concat([districts,water_source[cols[10:13]]], axis=1)
            lake_or_stream_water = lake_or_stream_water.drop(0)
            lake_or_stream_water.set_axis(column_names, axis=1, inplace=True)
            lake_or_stream_water = lake_or_stream_water.fillna(0)
            lake_or_stream_water = round(lake_or_stream_water,1)
            y = [lake_or_stream_water['Season A'][31],lake_or_stream_water['Season B'][31],lake_or_stream_water['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Lake/Stream Water'), font_color='red',titlefont_size=15,titlefont_color='green',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with source5:
           # 5. water catchment 
           water_catchment = pd.concat([districts,water_source[cols[13:]]], axis=1)
           water_catchment = water_catchment.drop(0)
           water_catchment.set_axis(column_names, axis=1, inplace=True)
           water_catchment = water_catchment.fillna(0)
           water_catchment = round(water_catchment,1)
           y = [water_catchment['Season A'][31],water_catchment['Season B'][31],water_catchment['Season C'][31]]
           fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

           fig.update_layout(title_text=(f'Water Catchment'), font_color='red',titlefont_size=15,titlefont_color='green',title_x = 0.1,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
           stl.plotly_chart(fig, use_container_width=True)

#  area under agriculture practices
    stl.subheader(':green[What Was Seasonal Change In Area under agricultural practices ?]')
    practices = survey_data.get('Table 10')
    cols = practices.columns
    p1,p2,p3 = stl.columns(3)
    with p1: 
        stl.text(round(practices[cols[1]][32]))
        stl.text(round(practices[cols[2]][32]))
        stl.text(round(practices[cols[3]][32]))
    with p2: 
        stl.text(round(practices[cols[4]][32]))
        stl.text(round(practices[cols[5]][32]))
    with p3: 
        stl.text(round(practices[cols[1]][32]))
        stl.text(round(practices[cols[2]][32]))
        stl.text(round(practices[cols[3]][32]))
    stl.write(practices)








































            
            
            
            




        
    