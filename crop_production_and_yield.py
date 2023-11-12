import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
import plotly.graph_objects as go





def crop_production_yeald(survey_data,igihe):

    trends = survey_data.get('Table 7')
    cols = trends.columns
    Years = cols[1:]
    color = ['yellow','bronze','#f6f2c5','#F5DEB3','cream','brown','red','green']
    fig = go.Figure()
    for i in range(0,14):
        # fig.add_scatter(x=Years, y= trends.iloc[i,1:], name=trends['Crops '][i])
        fig.add_trace(go.Scatter(x=Years,y=trends.iloc[i,1:], name=trends['Crops '][i]    # this sets its legend entry
        ))


    fig.update_layout(
        xaxis_title="Years",
        yaxis_title="Gross Value (Value RWF per ha)",
        legend_title="Main Crops",
        title_text = "Change In Gross Value Of Main Crops From 2016 - 2022",
        title_x =0.3, title_y=.9
        
        
    )

    stl.plotly_chart(fig, use_container_width=True)
    
    stl.write("What Was Overall Gross Value Per Year From 2016 To 2021 :question:")
    kpi1, kpi2,kpi3 = stl.columns(3)
    
    overall_216 =round(trends[cols[1]][14],0)
    kpi1.metric("2016","Overall GVA Was",f"{overall_216} RWF per ha")
    overall_2019 =round(trends[cols[4]][14],0)
    kpi1.metric("2019","Overall GVA Increased",f"{overall_2019} RWF per ha")
    
    overall_2017 =round(trends[cols[2]][14],0)
    kpi2.metric("2017","Overall GVA Increased",f"{overall_2017} RWF per ha")
    overall_2020 =round(trends[cols[5]][14],0)
    kpi2.metric("2020","Overall GVA Increased",f"{overall_2020} RWF per ha")
    
    overall_2018 =round(trends[cols[3]][14],0)
    kpi3.metric("2018","Overall GVA Increased",f"{overall_2018} RWF per ha")
    overall_2021 =round(trends[cols[6]][14],0)
    kpi3.metric("2021","Overall GVA Decreased")
    
    stl.subheader(":violet[What was seasonal change in agriculture land and it's percentage per district in 2022?]")

    selection1,selection2 = stl.columns([3,.5])
    new_cols = ['District','Total land area','Agricultural land','percentage of agricultural land']

    with selection1:
        season_land_use = survey_data.get('Table 8')
        districts = season_land_use['District'][:30]
        selected_districts = stl.multiselect('select district',districts)
        
    with selection2:
        season = stl.radio('Select Season',['Season A','Season B'])
   
    
    # getting districts
    dist = '' 

    for i in selected_districts:
        dist = dist + i +','
    if(selected_districts):
         if (season == 'Season A'):
            season_a_land_use = survey_data.get('Table 8')
            cols = season_a_land_use.columns
            data_to_be_used = round(season_a_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
            data_to_be_used = data_to_be_used[data_to_be_used['District'].isin(selected_districts)]

                
            plot = go.Figure(data=[go.Bar(
                
                name = 'Total Land Area',
                x = selected_districts,
                y = data_to_be_used['Total land area'],orientation='v',
                marker_color = 'green',
                text=[(f'{i}(1000 Ha)') for i in data_to_be_used['Total land area']],textposition='outside', 

                ),
                go.Bar(
                name = 'Agricultural land',
                x = selected_districts,
                y = data_to_be_used['Agricultural land'],orientation='v',
                marker_color = '#B0BF1A',
                text=[(f'{i}(1000 Ha)') for i in data_to_be_used['Agricultural land']],textposition='outside', 


                ),
                # go.Bar(
                # name = 'agricultural land %',
                # x = selected_districts,
                # y = data_to_be_used["percentage of agricultural land"],orientation='v',
                # marker_color = '#3EA99F',
                # text=[(f'{i}%') for i in data_to_be_used['percentage of agricultural land']],textposition='outside', 

                # )
            ])
            plot.update_traces(width=.5, marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
            plot.update_layout(
                title=(f'{season} 2022 Agricultural land in {dist} (,1000 Ha)') ,
                title_x=.26,
            width=200,
            height=500,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,), barmode='overlay'
            )
            
            plot.update_xaxes(tickfont=dict(family='Rockwell', color='crimson', size=14))
            stl.plotly_chart(plot,use_container_width=True)
        #     message
            if(selected_districts.__len__() == 1):
                 stl.write(f':ballot_box_with_check: In {dist} with total area land of :violet{[i for i in data_to_be_used["Total land area"]]} (1000 hecters), :green{[i for i in data_to_be_used["Agricultural land"]]} (1000 hecters) were used in agriculture and :red{[i for i in data_to_be_used["percentage of agricultural land"]]}% of agriculture land  were used in {season}')
            else:
               stl.write(f':ballot_box_with_check: In {dist} :green{[i for i in data_to_be_used["Agricultural land"]]} (1000 hecters) were used in agriculture and  :red{[i for i in data_to_be_used["percentage of agricultural land"]]}% of agriculture land  were used in {season}')

                  
         else:
            season_b_land_use = survey_data.get('Table 9')
            cols = season_b_land_use.columns
            data_to_be_used = round(season_b_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
            data_to_be_used = data_to_be_used[data_to_be_used['District'].isin(selected_districts)]

            plot = go.Figure(data=[go.Bar(
                
                name = 'Total Land Area',
                x = selected_districts,
                y = data_to_be_used['Total land area'],orientation='v',
                marker_color = '#2e8b57',
                text=[(f'{i} (1000 Ha)') for i in data_to_be_used['Total land area']],textposition='outside', 

                ),
                go.Bar(
                name = 'Agricultural land',
                x = selected_districts,
                y = data_to_be_used['Agricultural land'],orientation='v',
                marker_color = '#B0BF1A',
                text=[(f'{i} (1000 Ha)') for i in data_to_be_used['Agricultural land']],textposition='outside', 


                ),
                # go.Bar(
                # name = 'agricultural land %',
                # x = selected_districts,
                # y = data_to_be_used["percentage of agricultural land"],orientation='v',
                # marker_color = '#ffffff',
                # text=[(f'{i}%') for i in data_to_be_used['percentage of agricultural land']],textposition='outside', 

                # )
            ])
            plot.update_traces(width=.3, marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
            plot.update_layout(
                title=(f'{season} 2022 Agricultural land in {dist} (,1000 Ha)'),
                title_x=.26,
            width=3000,
            height=500,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),barmode='overlay'
            )
            
            plot.update_xaxes(tickfont=dict(family='Rockwell', color='crimson', size=14))
            stl.plotly_chart(plot,use_container_width=True)
            stl.write(f':ballot_box_with_check: In {dist} with total area land of :violet{[i for i in data_to_be_used["Total land area"]]} (1000 hecters), :green{[i for i in data_to_be_used["Agricultural land"]]} (1000 hecters) were used in agriculture and :red{[i for i in data_to_be_used["percentage of agricultural land"]]}% of agriculture land was used in {season}')

   
    else:
         seasonal_data  = ''
         if (season == 'Season A'):
            season_a_land_use = survey_data.get('Table 8')
            cols = season_a_land_use.columns
            data_to_be_used = round(season_a_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
            seasonal_data = data_to_be_used["Agricultural land"][30]
            plot = go.Figure(data=[go.Bar(
                
                name = 'Total Land Area',
                x = data_to_be_used['District'][:30].tolist(),
                y = data_to_be_used['Total land area'],orientation='v',
                marker_color = 'green',
                ),
                go.Bar(
                name = 'Agricultural land',
                x = data_to_be_used['District'][:30].tolist(),
                y = data_to_be_used['Agricultural land'],orientation='v',
                marker_color = '#B0BF1A',

                ),
                # go.Bar(
                # name = 'agricultural land %',
                # x = data_to_be_used['District'][:30].tolist(),
                # y = data_to_be_used["percentage of agricultural land"],orientation='v',
                # marker_color = '#3EA99F',
                # text=[(f'{i}%') for i in data_to_be_used['percentage of agricultural land']],textposition='auto', 

                # )
            ])
            plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
            plot.update_layout(
                title=(f'{season} 2022 Agricultural land use per district (,1000 Ha)'),
                title_x=.26,
            # width=3000,
            height=400,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),
            )
            
            plot.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='crimson', size=14))
            stl.plotly_chart(plot,use_container_width=True)
            stl.write(f':ballot_box_with_check: In {season} 2022, Agricultural land Was :green[{seasonal_data}(1000 Hecters)] And Covered :orange[{data_to_be_used["percentage of agricultural land"][30]} %] Of total Area Land.')
         else:
            season_b_land_use = survey_data.get('Table 9')
            cols = season_b_land_use.columns
            data_to_be_used = round(season_b_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
            plot = go.Figure(data=[go.Bar(
                
                name = 'Total Land Area',
                x = data_to_be_used['District'][:30].tolist(),
                y = data_to_be_used['Total land area'],orientation='v',
                marker_color = '#2e8b57',
                ),
                go.Bar(
                name = 'Agricultural land',
                x = data_to_be_used['District'][:30].tolist(),
                y = data_to_be_used['Agricultural land'],orientation='v',
                marker_color = '#B0BF1A',

                ),
                # go.Bar(
                # name = 'agricultural land %',
                # x = data_to_be_used['District'][:30].tolist(),
                # y = data_to_be_used["percentage of agricultural land"],orientation='v',
                # marker_color = '#ffffff',
                # text=[(f'{i}%') for i in data_to_be_used['percentage of agricultural land']],textposition='auto', 

                # )
            ])
            plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
            plot.update_layout(
                title=(f'{season} 2022 Agricultural land use per district (1000 Ha)'),
                title_x=.26,
            # width=3000,
            height=400,yaxis=dict( title='Land use per district (1000 Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),
            )
            
            plot.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='crimson', size=14))
            stl.plotly_chart(plot,use_container_width=True)
            stl.write(f' :ballot_box_with_check: Agricultural land Reduced From :green[1402.0(1000 Hecters)] In Season A To :blue[{data_to_be_used["Agricultural land"][30]}(1000 Hecters)] In Season B And \nCovered :orange[{data_to_be_used["percentage of agricultural land"][30]} %] Of total Area Land')

    stl.subheader(":green[Cultivated Area, Havested Area, Average Yield And Production Of Major crops]")
    
    if(igihe == 'Season A' or igihe ==None):
        stl.write('season A')
        # cultivated land
        cultivated_land = survey_data.get('Table 11')
        major = ['Cassava','Bananas','Irish potato','Sweet potato','Paddy rice','Maize','Beans']
        major_crops = round(cultivated_land[major])
        # havested land
        havested_land = survey_data.get('Table 14')
        havested_major_crops = round(havested_land[major])
        # average yield
        average_yield = survey_data.get('Table 17')
        yield_major_crops = round(average_yield[major])
        
    else:
        stl.write('season B')
        # cultivated land
        cultivated_land = survey_data.get('Table 12')
        major = ['Cassava','Bananas','Irish potato','Sweet potato','Paddy rice','Maize','Beans']
        major_crops = cultivated_land['major']
        major_crops = round(major_crops)
        # havested land
        havested_land = survey_data.get('Table 15')
        havested_major_crops = round(havested_land[major])
        # average yield
        average_yield = survey_data.get('Table 18')
        yield_major_crops = round(average_yield[major])
        
    
   
    stl.write(major_crops)
    stl.write(havested_major_crops)
    stl.write(yield_major_crops)
   
    col1,col2 = stl.columns(2)
    # with col1:
    
    
    # with col2:
    #     season_b_land_use = survey_data.get('Table 9')
    #     cols = season_b_land_use.columns
    #     data_to_be_used = round(season_b_land_use[cols[0:4]],1)
    #     stl.write(data_to_be_used)
        
   