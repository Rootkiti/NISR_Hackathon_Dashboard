import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
import plotly.graph_objects as go
# import main as m

survey_data = pd.read_excel("survey_data.xlsx", sheet_name=None)
location = pd.read_excel("provinces&district.xlsx", )


def showData(district,season):
    
    if(district != '' and season !=None):
        stl.subheader(f' % Of Agriculture Practices In {district}, {season} 2022')
    if(district !='' and season == None):  
        stl.subheader(f' % Of Agriculture Practices In {district}, Season A 2022')
    if(district == '' and season != None):
        stl.subheader(f' % Of Agriculture Practices  In {season} 2022 National Level')             
    if(district =='' and season ==None):
           stl.subheader(f' % Of Agriculture Practices  In Season A 2022 National Level')             
    x = ['Season A','Season B','Season C']
    col1,col2,col3,col4 = stl.columns(4)
    
    new_column_names = ['District','Overall','SSF','LSF']
    seasonal_practices = survey_data.get('Table 55')
    districts = seasonal_practices['District'].drop(0)

    cols = seasonal_practices.columns

    if (str(districts).strip().__contains__(district) and (district !='')):
        stl.write(f":green[Precentage of agriculture practices  in  {district} district 2022]")
        if(season == 'Seasoc A' or season == None):
            seasonal_practices = survey_data.get('Table 55')
            seasonal_practices = seasonal_practices.fillna(0)
            
        if (season == 'Season B'):
            seasonal_practices = survey_data.get('Table 56')
            seasonal_practices = seasonal_practices.fillna(0)

        if (season == 'Season C'):
            seasonal_practices = survey_data.get('Table 57')
            seasonal_practices = seasonal_practices.fillna(0)

        with col1:
            stl.write(':blue[Land Protection %]')
            protected_land = seasonal_practices[cols[0:4]]
            protected_land = protected_land.set_axis(new_column_names,axis=1)
            protected_land = protected_land.drop(0)
            protected_land_by_district = protected_land[protected_land['District']==district].reset_index()
            # drawing figue
            notation = round(protected_land_by_district['Overall'][0],1)
            data = [notation,(100-notation)]
            Lables = ['Achieved %','Lacking %']
            fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col2:
            stl.write(':blue[Use of Machinary (%)]')
            machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
            machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
            machinary_equipments = machinary_equipments.set_axis(new_column_names,axis=1)
            machinary_equipments_by_district = machinary_equipments[machinary_equipments['District'] == district].reset_index()
            # drawing figue
            notation = round(machinary_equipments_by_district['Overall'][0],1)
            data = [notation,(100-notation)]
            Lables = ['Achieved %','Lacking %']
            fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True)

        with col3:
            stl.write(':blue[Irrigation (%)]')
            irrigation = seasonal_practices[cols[7:10]].drop(0)
            irrigation = pd.concat([districts,irrigation], axis=1)
            irrigation = irrigation.set_axis(new_column_names,axis=1)
            irrigation_by_district = irrigation[irrigation['District'] == district].reset_index()
            # drawing figue
            notation = round(irrigation_by_district['Overall'][0],1)
            data = [notation,(100-notation)]
            Lables = ['Achieved %','Lacking %']
            fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
            fig.update_traces(hoverinfo='percent+label', textinfo='none')
            fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
            stl.plotly_chart(fig,use_container_width=True) 
                    
        with col4:
                stl.write(':blue[Agroforestry (%)]')
                agroforestry = seasonal_practices[cols[10:]].drop(0)
                agroforestry = pd.concat([districts,agroforestry], axis=1)
                agroforestry = agroforestry.set_axis(new_column_names,axis=1)
                agroforestry_by_district = agroforestry[agroforestry['District'] == district].reset_index()
                # drawing figue
                notation = round(agroforestry_by_district['Overall'][0],1)
                data = [notation,(100-notation)]
                Lables = ['Achieved %','Lacking %']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(hoverinfo='percent+label', textinfo='none')
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=20, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)            
        # # message
        stl.write(f':pushpin:  In {" Season A" if season == None else season} 2022, land protection against erosion achieved was :red[{round(protected_land_by_district["Overall"][0],1)}%] with  :green[{round(protected_land_by_district["SSF"][0],1)}%] of small scale farmers and :blue[{round(protected_land_by_district["LSF"][0],1)}%] of larger scale farmers.')
        stl.write(f':pushpin: use of machinary in agriculture was :red[{round(machinary_equipments_by_district["Overall"][0],1)}%] with  :green[{round(machinary_equipments_by_district["SSF"][0],1)}%] of small scale farmers and :blue[{round(machinary_equipments_by_district["LSF"][0],1)}%] of larger scale farmers.')
        stl.write(f':pushpin: Irrigation was :red[{round(irrigation_by_district["Overall"][0],1)}%] with  :green[{round(irrigation_by_district["SSF"][0],1)}%] of small scale farmers and :blue[{round(irrigation_by_district["LSF"][0],1)}%] of larger scale farmers.')
        stl.write(f':pushpin: Agroforestry was :red[{round(agroforestry_by_district["Overall"][0],1)}%] with  :green[{round(agroforestry_by_district["SSF"][0],1)}%] of small scale farmers and :blue[{round(agroforestry_by_district["LSF"][0],1)}%] of larger scale farmers.')

    else:
        stl.write(f"##### :green[**Precentage of agriculture practices at national level in 2022**]")

        if(season == 'Season A' or season ==None):
                with col1:
                    stl.write(':blue[Land protection (%)]')
                    protected_land = seasonal_practices[cols[0:4]]
                    protected_land = protected_land.set_axis(new_column_names,axis=1)
                    protected_land = protected_land.drop(0)
                    ## drawing figue
                    data = [round(protected_land['Overall'][31],1),round((100-protected_land['Overall'][31]),1)]
                    notation = protected_land['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')
                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)

                with col2:
                    stl.write(':blue[Use of Machinary (%)]')
                    machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
                    machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
                    machinary_equipments = machinary_equipments.set_axis(new_column_names,axis=1)
                        ## drawing figue
                    data = [round(machinary_equipments['Overall'][31],1),round((100-machinary_equipments['Overall'][31]),1)]
                    notation = machinary_equipments['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')
                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)

                with col3:
                    stl.write(':blue[Irrigation (%)]')
                    irrigation = seasonal_practices[cols[7:10]].drop(0)
                    irrigation = pd.concat([districts,irrigation], axis=1)
                    irrigation = irrigation.set_axis(new_column_names,axis=1)
                    ## drawing figue
                    data = [round(irrigation['Overall'][31],1),round((100-irrigation['Overall'][31]),1)]
                    notation = irrigation['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')

                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)
                
                with col4:
                    stl.write(':blue[Agroforestry (%)]')
                    agroforestry = seasonal_practices[cols[10:]].drop(0)
                    agroforestry = pd.concat([districts,agroforestry], axis=1)
                    agroforestry = agroforestry.set_axis(new_column_names,axis=1)
                    ## drawing figue
                    data = [round(agroforestry['Overall'][31],1),round((100-agroforestry['Overall'][31]),1)]
                    notation = agroforestry['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')

                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)
                # message
                stl.write(f':pushpin: In season A 2022, land protection against erosion achieved was :orange[{round(protected_land["Overall"][31],1)}%] with  :green[{round(protected_land["SSF"][31],1)}%] of small scale farmers and :blue[{round(protected_land["LSF"][31],1)}%] of larger scale farmers.')
                stl.write(f':pushpin: use of machinary in agriculture was :orange[{round(machinary_equipments["Overall"][31],1)}%] with  :green[{round(machinary_equipments["SSF"][31],1)}%] of small scale farmers and :blue[{round(machinary_equipments["LSF"][31],1)}%] of larger scale farmers.')
                stl.write(f':pushpin: Irrigation was :orange[{round(irrigation["Overall"][31],1)}%] with  :green[{round(irrigation["SSF"][31],1)}%] of small scale farmers and :blue[{round(irrigation["LSF"][31],1)}%] of larger scale farmers.')
                stl.write(f':pushpin: Agroforestry was :orange[{round(agroforestry["Overall"][31],1)}%] with  :green[{round(agroforestry["SSF"][31],1)}%] of small scale farmers and :blue[{round(agroforestry["LSF"][31],1)}%] of larger scale farmers.')

        
        if(season == 'Season B'):
            seasonal_practices = survey_data.get('Table 56')
            with col1:
                stl.write(':blue[Land Protection (%)]')
                protected_land = seasonal_practices[cols[0:4]]
                protected_land = protected_land.set_axis(new_column_names,axis=1)
                protected_land = protected_land.drop(0)
                ## drawing figue
                data = [round(protected_land['Overall'][31],1),round((100-protected_land['Overall'][31]),1)]
                notation = protected_land['Overall'][31]
                Lables = ['Achieved %','Lacking %']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(hoverinfo='percent+label', textinfo='none')
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)

            with col2:
                stl.write(':blue[Use Of Machinary (%)]')
                machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
                machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
                machinary_equipments = machinary_equipments.set_axis(new_column_names,axis=1)
                    ## drawing figue
                data = [round(machinary_equipments['Overall'][31],1),round((100-machinary_equipments['Overall'][31]),1)]
                notation = machinary_equipments['Overall'][31]
                Lables = ['Achieved %','Lacking %']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(hoverinfo='percent+label', textinfo='none')
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)

            with col3:
                stl.write(':blue[Irrigation (%)]')
                irrigation = seasonal_practices[cols[7:10]].drop(0)
                irrigation = pd.concat([districts,irrigation], axis=1)
                irrigation = irrigation.set_axis(new_column_names,axis=1)
                ## drawing figue
                data = [round(irrigation['Overall'][31],1),round((100-irrigation['Overall'][31]),1)]
                notation = irrigation['Overall'][31]
                Lables = ['Achieved %','Lacking %']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(hoverinfo='percent+label', textinfo='none')

                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
            
            with col4:
                stl.write(':blue[agroforestry (%)]')
                agroforestry = seasonal_practices[cols[10:]].drop(0)
                agroforestry = pd.concat([districts,agroforestry], axis=1)
                agroforestry = agroforestry.set_axis(new_column_names,axis=1)
                ## drawing figue
                data = [round(agroforestry['Overall'][31],1),round((100-agroforestry['Overall'][31]),1)]
                notation = agroforestry['Overall'][31]
                Lables = ['Achieved %','Lacking %']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(hoverinfo='percent+label', textinfo='none')

                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
            
        # message
            stl.write(f':pushpin: In {season} 2022, land protection against erosion achieved was :orange[{round(protected_land["Overall"][31],1)}%] with a decrease of :orange[0.7%] compared to season A.  :green[{round(protected_land["SSF"][31],1)}%] were small scale farmers and :blue[{round(protected_land["LSF"][31],1)}%] of larger scale farmers.')
            stl.write(f':pushpin: use of machinary in agriculture was :orange[{round(machinary_equipments["Overall"][31],1)}%] and there was a decreas of :orange[0.1%] compared to season A.  :green[{round(machinary_equipments["SSF"][31],1)}%] were small scale farmers and :blue[{round(machinary_equipments["LSF"][31],1)}%] of larger scale farmers.')
            stl.write(f':pushpin: Irrigation was :orange[{round(irrigation["Overall"][31],1)}%] with a decrease of :orange[0.2%] compared to season A.  :green[{round(irrigation["SSF"][31],1)}%] were small scale farmers and :blue[{round(irrigation["LSF"][31],1)}%] of larger scale farmers.')
            stl.write(f':pushpin: Agroforestry was :orange[{round(agroforestry["Overall"][31],1)}%] with a decrease of :orange[4.35%].  :green[{round(agroforestry["SSF"][31],1)}%] were small scale farmers and :blue[{round(agroforestry["LSF"][31],1)}%] of larger scale farmers.')

        if (season == 'Season C'):
                seasonal_practices = survey_data.get('Table 57')
                with col1:
                    stl.write(':blue[Land Protection (%)]')
                    protected_land = seasonal_practices[cols[0:4]]
                    protected_land = protected_land.set_axis(new_column_names,axis=1)
                    protected_land = protected_land.drop(0)
                    ## drawing figue
                    data = [round(protected_land['Overall'][31],1),round((100-protected_land['Overall'][31]),1)]
                    notation = protected_land['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')
                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)

                with col2:
                    stl.write(':blue[Use Of Machnary (%)]')
                    machinary_equipments = seasonal_practices[cols[4:7]].drop(0)
                    machinary_equipments = pd.concat([districts,machinary_equipments], axis=1)
                    machinary_equipments = machinary_equipments.set_axis(new_column_names,axis=1)
                        ## drawing figue
                    data = [round(machinary_equipments['Overall'][31],1),round((100-machinary_equipments['Overall'][31]),1)]
                    notation = machinary_equipments['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')
                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)

                with col3:
                    stl.write(':blue[Irrigation %]')
                    irrigation = seasonal_practices[cols[7:10]].drop(0)
                    irrigation = pd.concat([districts,irrigation], axis=1)
                    irrigation = irrigation.set_axis(new_column_names,axis=1)
                    ## drawing figue
                    data = [round(irrigation['Overall'][31],1),round((100-irrigation['Overall'][31]),1)]
                    notation = irrigation['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')

                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)
                
                with col4:
                    stl.write(':blue[Agroforestry (%)]')
                    agroforestry = seasonal_practices[cols[10:]].drop(0)
                    agroforestry = pd.concat([districts,agroforestry], axis=1)
                    agroforestry = agroforestry.set_axis(new_column_names,axis=1)
                    ## drawing figue
                    data = [round(agroforestry['Overall'][31],1),round((100-agroforestry['Overall'][31]),1)]
                    notation = agroforestry['Overall'][31]
                    Lables = ['Achieved %','Lacking %']
                    fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                    color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                    fig.update_traces(hoverinfo='percent+label', textinfo='none')

                    fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{round(notation,1)}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                    stl.plotly_chart(fig,use_container_width=True)
        
                    # message
                stl.write(f':pushpin: In {season} 2022, land protection against erosion achieved was :orange[{round(protected_land["Overall"][31],1)}%] with an increase of :orange[3.7%] compared to season A and :rainbow[4.4%] compared to season B.  :green[{round(protected_land["SSF"][31],1)}%] were small scale farmers and :blue[{round(protected_land["LSF"][31],1)}%] of site.')
                stl.write(f':pushpin: use of machinary in agriculture was :orange[{round(machinary_equipments["Overall"][31],1)}%] and there was a decreas of :orange[0.4%] compared to season A and :rainbow[0.3%] compared to season B.  :green[{round(machinary_equipments["SSF"][31],1)}%] were small scale farmers and :blue[{round(machinary_equipments["LSF"][31],1)}%] of site.')
                stl.write(f':pushpin: Irrigation was :orange[{round(irrigation["Overall"][31],1)}%] with an increase of :orange[54.7%] compared to season A and :rainbow[54.9%] compared to season B.  :green[{round(irrigation["SSF"][31],1)}%] were small scale farmers and :blue[{round(irrigation["LSF"][31],1)}%] of site.')
                stl.write(f':pushpin: Agroforestry was :orange[{round(agroforestry["Overall"][31],1)}%] with a decrease of :orange[27%] compared to season A and :rainbow[22.8%] compared to season B.  :green[{round(agroforestry["SSF"][31],1)}%] were small scale farmers.')

    stl.write(':point_left: Use side menu to filter by season and/or district.')
     








    # Use of modern irrigation methides
    if(district == ''):
        stl.markdown('#### :bar_chart: % Use Of Modern Irrigation Methods Per Season In 2022') 
        stl.write(f"##### :green[Precentage of seasonal use of mordern irrigation methods at national level]")

    else:
        stl.markdown(f'#### :bar_chart: % Use Of Modern Irrigation Methods Per Season In {district} District 2022')  
        stl.write(f"##### :green[Precentage of seasonal use of mordern irrigation methods at District level]")

            
#   types of irrigation section
    type1,type2,type3,type4,type5= stl.columns(5)
    irrigation_type = survey_data.get("Table 58")
    irrigation_type.drop(0)
    clrs = ['#00628e','#49abc8','#358a9a']
    cols = irrigation_type.columns
    
    if str(districts).strip().__contains__(district) and (district !=''):
        
        value = district
        with type1:            
            # surface irrigation
            Surface_irrigation = irrigation_type[cols[:4]]
            n_cols = ['District','Season A','Season B','Season C']
            Surface_irrigation = Surface_irrigation.set_axis(n_cols,axis=1)
            Surface_irrigation = Surface_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Surface_irrigation = Surface_irrigation.fillna(0)
            district_Surface_irrigation = Surface_irrigation[Surface_irrigation['District'] == district]
            district_Surface_irrigation = round(district_Surface_irrigation,1)
            y = [district_Surface_irrigation['Season A'].sum(),district_Surface_irrigation['Season B'].sum(),district_Surface_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Surface Irrigation', font_color='white',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type2:
            # flood irrigation
            Flood_irrigation = irrigation_type[cols[4:7]]
            Flood_irrigation = pd.concat([irrigation_type['District'].drop(0),Flood_irrigation],axis=1)
            Flood_irrigation = Flood_irrigation.set_axis(n_cols,axis=1)
            Flood_irrigation = Flood_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Flood_irrigation = Flood_irrigation.fillna(0)
            Flood_irrigation = round(Flood_irrigation,1)
            district_Flood_irrigation = Flood_irrigation[Flood_irrigation['District']==district]
            y = [district_Flood_irrigation['Season A'].sum(),district_Flood_irrigation['Season B'].sum(),district_Flood_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Flood Irrigation', font_color='white',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type3:
            # Drip irrigation
            Drip_irrigation = irrigation_type[cols[7:10]]
            Drip_irrigation = pd.concat([irrigation_type['District'].drop(0),Drip_irrigation],axis=1)
            Drip_irrigation = Drip_irrigation.set_axis(n_cols,axis=1)
            Drip_irrigation = Drip_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Drip_irrigation = Drip_irrigation.fillna(0)
            Drip_irrigation = round(Drip_irrigation,1)
            district_Drip_irrigation = Drip_irrigation[Drip_irrigation['District'] == district]
            y = [district_Drip_irrigation['Season A'].sum(),district_Drip_irrigation['Season B'].sum(),district_Drip_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Drip Irrigation', font_color='white',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type4:

            # Sprinkler irrigation
            Sprinkle_irrigation = irrigation_type[cols[10:13]]
            Sprinkle_irrigation = pd.concat([irrigation_type['District'].drop(0),Sprinkle_irrigation],axis=1)
            Sprinkle_irrigation = Sprinkle_irrigation.set_axis(n_cols,axis=1)
            Sprinkle_irrigation = Sprinkle_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Sprinkle_irrigation = Sprinkle_irrigation.fillna(0)
            Sprinkle_irrigation = round(Sprinkle_irrigation,1)
            district_Sprinkle_irrigation = Sprinkle_irrigation[Sprinkle_irrigation['District'] == district]
            
            y = [district_Sprinkle_irrigation['Season A'].sum(),district_Sprinkle_irrigation['Season B'].sum(),district_Sprinkle_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Sprinkler Irrigation', font_color='white',titlefont_size=15,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                 ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type5:
            # Pivot irrigation
            Pivot_irrigation = irrigation_type[cols[13:16]]
            Pivot_irrigation = pd.concat([irrigation_type['District'].drop(0),Pivot_irrigation],axis=1)
            Pivot_irrigation = Pivot_irrigation.set_axis(n_cols,axis=1)
            Pivot_irrigation = Pivot_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Pivot_irrigation = Pivot_irrigation.fillna(0)
            Pivot_irrigation = round(Pivot_irrigation,1)
            district_Pivot_irrigation = Pivot_irrigation[Pivot_irrigation['District'] == district]
            
            y = [district_Pivot_irrigation['Season A'].sum(),district_Pivot_irrigation['Season B'].sum(),district_Pivot_irrigation['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f'Pivot Irrigation', font_color='white',titlefont_size=15,yaxis=dict(
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
            Surface_irrigation = Surface_irrigation.set_axis(n_cols,axis=1)
            Surface_irrigation = Surface_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Surface_irrigation = Surface_irrigation.fillna(0)
            Surface_irrigation = round(Surface_irrigation,1)
            y = [Surface_irrigation['Season A'][30],Surface_irrigation['Season B'][30],Surface_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside',)])

            fig.update_layout(title_text=(f'Surface Irrigation'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

        with type2:            
            # flood irrigation
            Flood_irrigation = irrigation_type[cols[4:7]]
            Flood_irrigation = pd.concat([irrigation_type['District'].drop(0),Flood_irrigation],axis=1)
            Flood_irrigation = Flood_irrigation.set_axis(n_cols,axis=1)
            Flood_irrigation = Flood_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Flood_irrigation = Flood_irrigation.fillna(0)
            Flood_irrigation = round(Flood_irrigation,1)
            y = [Flood_irrigation['Season A'][30],Flood_irrigation['Season B'][30],Flood_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Flood Irrigation'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type3:
            # Drip irrigation
            Drip_irrigation = irrigation_type[cols[7:10]]
            Drip_irrigation = pd.concat([irrigation_type['District'].drop(0),Drip_irrigation],axis=1)
            Drip_irrigation = Drip_irrigation.set_axis(n_cols,axis=1)
            Drip_irrigation = Drip_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Drip_irrigation = Drip_irrigation.fillna(0)
            Drip_irrigation = round(Drip_irrigation,1)
            y = [Drip_irrigation['Season A'][30],Drip_irrigation['Season B'][30],Drip_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Flood Irrigation'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type4:

            # Sprinkler irrigation
            Sprinkle_irrigation = irrigation_type[cols[10:13]]
            Sprinkle_irrigation = pd.concat([irrigation_type['District'].drop(0),Sprinkle_irrigation],axis=1)
            Sprinkle_irrigation = Sprinkle_irrigation.set_axis(n_cols,axis=1)
            Sprinkle_irrigation = Sprinkle_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Sprinkle_irrigation = Sprinkle_irrigation.fillna(0)
            Sprinkle_irrigation = round(Sprinkle_irrigation,1)
            y = [Sprinkle_irrigation['Season A'][30],Sprinkle_irrigation['Season B'][30],Sprinkle_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Sprinkler Irrigation'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with type5:
            # Pivot irrigation
            Pivot_irrigation = irrigation_type[cols[13:16]]
            Pivot_irrigation = pd.concat([irrigation_type['District'].drop(0),Pivot_irrigation],axis=1)
            Pivot_irrigation = Pivot_irrigation.set_axis(n_cols,axis=1)
            Pivot_irrigation = Pivot_irrigation.drop([0,1]).reset_index().drop(columns=['index'])
            Pivot_irrigation = Pivot_irrigation.fillna(0)
            Pivot_irrigation = round(Pivot_irrigation,1)
            y = [Pivot_irrigation['Season A'][30],Pivot_irrigation['Season B'][30],Pivot_irrigation['Season C'][30]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=clrs,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Pivot Irrigation'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
    stl.write(':point_left: Select district from left sidebar to see use of modern irrigation methids in  desired district per season.')
   
   
   
    if(district == ''):
       stl.markdown('####  :bar_chart: % Of Each Source Of Water Used In Irrigation Per Season In 2022')  
       stl.write(f"##### :green[Precentage of seasonal use and source of water for  irrigation at national level]")

    else:
        stl.markdown(f'#### :bar_chart: % Of Each Source Of Water Used In Irrigation Per Season In {district} District 2022')
        stl.write(f"##### :green[Precentage of seasonal use and source of water for  irrigation at District level]")
  

    
   #  source of water used in irrigation activities
    source1,source2,source3,source4,source5 = stl.columns(5)
    water_source = survey_data.get('Table 59')
    cols = water_source.columns
    districts = water_source[cols[0]]
    column_names = ['District',	'Season A',	'Season B',	'Season C']
    colors = ['#00628e','#49abc8','#358a9a']
    


    if str(districts).strip().__contains__(district) and (district !=''):
        
        with source1:
            # 1. Rain water
            rainwater = water_source[cols[:4]]
            rainwater = rainwater.drop(0)
            rainwater = rainwater.set_axis(column_names, axis=1)
            rainwater = rainwater.fillna(0)
            rainwater = round(rainwater,1)
            rainwater_per_district = rainwater[rainwater['District'] == district]
            y = [rainwater_per_district['Season A'].sum(),rainwater_per_district['Season B'].sum(),rainwater_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Rain Water'), font_color='white',titlefont_size=15, titlefont_color='#3090C7', yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

            
        with source2:
            
            water_treatment = pd.concat([districts,water_source[cols[4:7]]], axis=1)
            water_treatment = water_treatment.drop(0)
            water_treatment = water_treatment.set_axis(column_names, axis=1)
            water_treatment = water_treatment.fillna(0)
            water_treatment = round(water_treatment,1)
            water_treatment_per_district = water_treatment[water_treatment['District'] == district]
            y = [water_treatment_per_district['Season A'].sum(),water_treatment_per_district['Season B'].sum(),water_treatment_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title=f' Water treatment', font_color='white',titlefont_size=15, titlefont_color='#3090C7', yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
            ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source3:
            # 3. underground water
            underground_water = pd.concat([districts,water_source[cols[7:10]]], axis=1)
            underground_water = underground_water.drop(0)
            underground_water = underground_water.set_axis(column_names, axis=1)
            underground_water = underground_water.fillna(0)
            underground_water = round(underground_water,1)
            underground_water_per_district = underground_water[underground_water['District'] == district]
            y = [underground_water_per_district['Season A'].sum(),underground_water_per_district['Season B'].sum(),underground_water_per_district['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=f'Underground Water', font_color='white',titlefont_size=13, titlefont_color='#3090C7', yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
              ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source4:
            # 4. lake/stream water
            lake_or_stream_water = pd.concat([districts,water_source[cols[10:13]]], axis=1)
            lake_or_stream_water = lake_or_stream_water.drop(0)
            lake_or_stream_water = lake_or_stream_water.set_axis(column_names, axis=1)
            lake_or_stream_water = lake_or_stream_water.fillna(0)
            lake_or_stream_water = round(lake_or_stream_water,1)
            lake_or_stream_water_perdistrict = lake_or_stream_water[lake_or_stream_water['District'] == district]
            y = [lake_or_stream_water_perdistrict['Season A'].sum(),lake_or_stream_water_perdistrict['Season B'].sum(),lake_or_stream_water_perdistrict['Season C'].sum()]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=f'Lake / streams Water', font_color='white',titlefont_size=13, titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
               ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source5:
           # 5. water catchment 
           water_catchment = pd.concat([districts,water_source[cols[13:]]], axis=1)
           water_catchment = water_catchment.drop(0)
           water_catchment = water_catchment.set_axis(column_names, axis=1)
           water_catchment = water_catchment.fillna(0)
           water_catchment = round(water_catchment,1)
           water_catchment_per_district = water_catchment[water_catchment['District'] == district]
           y = [water_catchment_per_district['Season A'].sum(),water_catchment_per_district['Season B'].sum(),water_catchment_per_district['Season C'].sum()]
           fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
           textposition='outside')])

           fig.update_layout(title_text=f'Water catchment', font_color='white',titlefont_size=15,titlefont_color='#3090C7',  yaxis=dict(
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
            rainwater = rainwater.set_axis(column_names, axis=1)
            rainwater = rainwater.fillna(0)
            rainwater = round(rainwater,1)
            y = [rainwater['Season A'][31],rainwater['Season B'][31],rainwater['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y], 
            textposition='outside')])

            fig.update_layout(title_text=('Rain Water'), titlefont_size=15,titlefont_color='#3090C7',title_x = 0.3,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                                
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
            
        with source2:
            # 2. water treatment
            water_treatment = pd.concat([districts,water_source[cols[4:7]]], axis=1)
            water_treatment = water_treatment.drop(0)
            water_treatment = water_treatment.set_axis(column_names, axis=1)
            water_treatment = water_treatment.fillna(0)
            water_treatment = round(water_treatment,1)
            y = [water_treatment['Season A'][31],water_treatment['Season B'][31],water_treatment['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Water Treatment'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',title_x = 0.2,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ))
            stl.plotly_chart(fig, use_container_width=True)

        with source3:            # 3. underground water
            underground_water = pd.concat([districts,water_source[cols[7:10]]], axis=1)
            underground_water = underground_water.drop(0)
            underground_water = underground_water.set_axis(column_names, axis=1)
            underground_water = underground_water.fillna(0)
            underground_water = round(underground_water,1)
            y = [underground_water['Season A'][31],underground_water['Season B'][31],underground_water['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'underground Water'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',title_x = 0.1,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)

        with source4:
            # 4. lake/stream water
            lake_or_stream_water = pd.concat([districts,water_source[cols[10:13]]], axis=1)
            lake_or_stream_water = lake_or_stream_water.drop(0)
            lake_or_stream_water = lake_or_stream_water.set_axis(column_names, axis=1,)
            lake_or_stream_water = lake_or_stream_water.fillna(0)
            lake_or_stream_water = round(lake_or_stream_water,1)
            y = [lake_or_stream_water['Season A'][31],lake_or_stream_water['Season B'][31],lake_or_stream_water['Season C'][31]]
            fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

            fig.update_layout(title_text=(f'Lake/Stream Water'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
            stl.plotly_chart(fig, use_container_width=True)
        with source5:
           # 5. water catchment 
           water_catchment = pd.concat([districts,water_source[cols[13:]]], axis=1)
           water_catchment = water_catchment.drop(0)
           water_catchment = water_catchment.set_axis(column_names, axis=1)
           water_catchment = water_catchment.fillna(0)
           water_catchment = round(water_catchment,1)
           y = [water_catchment['Season A'][31],water_catchment['Season B'][31],water_catchment['Season C'][31]]
           fig = go.Figure([go.Bar(x=x, y=y,marker_color=colors,text=[(f'{i}%') for i in y],
            textposition='outside')])

           fig.update_layout(title_text=(f'Water Catchment'), font_color='white',titlefont_size=15,titlefont_color='#3090C7',title_x = 0.1,yaxis=dict(
                                title='Percentage (%)',
                                titlefont_size=15,
                                tickfont_size=14,
                           ),)
           stl.plotly_chart(fig, use_container_width=True)
    stl.write(':point_left: Select district from left sidebar to see sources of water used in desired district per season.')
#  area under agriculture practices
    stl.subheader(':bar_chart: Seasonal Change In Area under agricultural practices in 20222')
    practices = survey_data.get('Table 10')
    cols = practices.columns
    practice = [' Agricultural land under Modern irrigation (Ha)','Agricultural area under erosion control','Agricultural area under agroforestry trees']
    p1,p2,p3 = stl.columns(3)
    a_data = [round(practices[cols[1]][32]),round(practices[cols[4]][32]),round(practices[cols[7]][32])]
    b_data = [round(practices[cols[2]][32]),round(practices[cols[5]][32]),round(practices[cols[8]][32])]
    c_data = [round(practices[cols[3]][32]),0,0]
    # with p1: 
 
        
    seasons_bar = go.Figure(data=[go.Bar(
                
                name = 'Season A',
                x = practice,
                y = a_data,orientation='v',
                marker_color = '#00628e',
                text=[(f'{i} Ha') for i in a_data],textposition='outside', 

                ),
                go.Bar(
                name = 'Season B',
                x = practice,
                y = b_data,orientation='v',
                marker_color = '#49abc8',
                text=[(f'{i} Ha') for i in b_data],textposition='outside', 


                ),
                go.Bar(
                name = 'Season C',
                x = practice,
                y = c_data,orientation='v',
                marker_color = '#358a9a',
                text=[(f'{i} Ha') for i in c_data],textposition='auto', 

                )
            ])
    seasons_bar.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
    seasons_bar.update_layout(
                title=(f'Seasonal Change In Area under agricultural practices'),
                title_x=.26,
            # width=3000,
            height=600,yaxis=dict( title='Land Size (Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Agriculture Practice',titlefont_size=15,tickfont_size=14,),barmode='group'
            )
            
    seasons_bar.update_xaxes(tickangle=15, tickfont=dict(family='Rockwell', color='white', size=14))
    stl.plotly_chart(seasons_bar,use_container_width=True)
    stl.write(f':pushpin: Modern irrigation was used on :green[27,134] hecters in season A and it was decreased to :orange[21,096] hecters in season B and in season C it was decresed to :violet[1,148] hecters.')
    stl.write(f':pushpin: Erosion control was applied to :green[996,156] hecters in season A and decreased to  :orange[967,224] hecters in season B.')
    stl.write(f':pushpin: Agroforestry was applied to :green[618,044] hecters in season A and increased to :orange[684,921] hecters in season B.')

        

    
            
            
            




        
    