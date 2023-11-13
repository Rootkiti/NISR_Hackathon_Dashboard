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
        legend_title="Major Crops",
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

    stl.subheader(":bar_chart: :green[Average Yield Of Major crops Per Season In 2022]")
    
    if(igihe == 'Season A' or igihe ==None):
        # cultivated land
        cultivated_land = survey_data.get('Table 11')
        major = ['Cassava','Bananas','Irish potato','Sweet potato','Paddy rice','Maize','Beans']
        a_major_crops = round(cultivated_land[major])
        # lables = ['National','SSF','LSF']
        # a_data = [major_crops['Cassava'][30],major_crops['Cassava'][31],major_crops['Cassava'][32],]
        # havested land
        havested_land = survey_data.get('Table 14')
        a_havested_major_crops = round(havested_land[major])
        # average yield
        average_yield = survey_data.get('Table 17')
        a_yield_major_crops = round(average_yield[major])
        
        a_national = [a_yield_major_crops['Cassava'][30],a_yield_major_crops['Bananas'][30],a_yield_major_crops['Irish potato'][30],a_yield_major_crops['Sweet potato'][30],a_yield_major_crops['Paddy rice'][30],a_yield_major_crops['Maize'][30],a_yield_major_crops['Beans'][30]]
        a_ssf = [a_yield_major_crops['Cassava'][31],a_yield_major_crops['Bananas'][31],a_yield_major_crops['Irish potato'][31],a_yield_major_crops['Sweet potato'][31],a_yield_major_crops['Paddy rice'][31],a_yield_major_crops['Maize'][31],a_yield_major_crops['Beans'][31]]
        a_lsf = [a_yield_major_crops['Cassava'][32],a_yield_major_crops['Bananas'][32],a_yield_major_crops['Irish potato'][32],a_yield_major_crops['Sweet potato'][32],a_yield_major_crops['Paddy rice'][32],a_yield_major_crops['Maize'][32],a_yield_major_crops['Beans'][32]]

        plot = go.Figure(data=[go.Bar(
                
                name = 'National',
                y = major,
                x = a_national,orientation='h',
                marker_color = 'blue',
                text=[(f'{i}Kg/Ha') for i in a_national],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'Small Scale farmers',
                y = major,
                x = a_ssf,orientation='h',
                marker_color = 'green',
                text=[(f'{i}Kg/Ha') for i in a_ssf],textposition='outside',textfont_size=20, 


                ),
                go.Bar(
                name = 'Larger scale Farmers',
                y = major,
                x = a_lsf,orientation='h',
                marker_color = 'yellow',
                text=[(f'{i}Kg/Ha') for i in a_lsf],textposition='outside'

                )
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'{season} 2022 Average yield Of Major Crops'),
                title_x=.26,
            width=600,
            height=600,yaxis=dict( title='Major Crops', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Kg\Ha',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        
       

    if(igihe == 'Season B'):
        # cultivated land
        cultivated_land = survey_data.get('Table 12 ')
        major = ['Cassava','Bananas','Irish potato','Sweet potato','Paddy rice','Maize','Beans']
        major_crops = cultivated_land[major]
        b_major_crops = round(major_crops)
        # havested land
        havested_land = survey_data.get('Table 15 ')
        b_havested_major_crops = round(havested_land[major])
        # average yield
        average_yield = survey_data.get('Table 18 ')
        b_yield_major_crops = round(average_yield[major])
        
        b_national = [b_yield_major_crops['Cassava'][30],b_yield_major_crops['Bananas'][30],b_yield_major_crops['Irish potato'][30],b_yield_major_crops['Sweet potato'][30],b_yield_major_crops['Paddy rice'][30],b_yield_major_crops['Maize'][30],b_yield_major_crops['Beans'][30]]
        b_ssf = [b_yield_major_crops['Cassava'][31],b_yield_major_crops['Bananas'][31],b_yield_major_crops['Irish potato'][31],b_yield_major_crops['Sweet potato'][31],b_yield_major_crops['Paddy rice'][31],b_yield_major_crops['Maize'][31],b_yield_major_crops['Beans'][31]]
        b_lsf = [b_yield_major_crops['Cassava'][32],b_yield_major_crops['Bananas'][32],b_yield_major_crops['Irish potato'][32],b_yield_major_crops['Sweet potato'][32],b_yield_major_crops['Paddy rice'][32],b_yield_major_crops['Maize'][32],b_yield_major_crops['Beans'][32]]

        plot = go.Figure(data=[go.Bar(
                
                name = 'National',
                y = major,
                x = b_national,orientation='h',
                marker_color = 'blue',
                text=[(f'{i}Kg/Ha') for i in b_national],textposition='outside',textfont_size=20, 

                ),
                go.Bar(
                name = 'Small Scale farmers',
                y = major,
                x = b_ssf,orientation='h',
                marker_color = 'green',
                text=[(f'{i}Kg/Ha') for i in b_ssf],textposition='outside',textfont_size=20, 


                ),
                go.Bar(
                name = 'Larger scale Farmers',
                y = major,
                x = b_lsf,orientation='h',
                marker_color = 'yellow',
                text=[(f'{i}Kg/Ha') for i in b_lsf],textposition='outside',

                )
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'{igihe} 2022 Average yield Of Major Crops'),
                title_x=.26,
            width=600,
            height=600,yaxis=dict( title='Major Crops', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Kg\Ha',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
    if(igihe == 'Season C'):
        # cultivated land
        cultivated_land = survey_data.get('Table 13')
        major = ['Irish potato','Sweet potato','Beans']
        major_crops = cultivated_land[major]
        C_major_crops = round(major_crops)
        # havested land
        havested_land = survey_data.get('Table 16')
        c_havested_major_crops = round(havested_land[major])
        # average yield
        average_yield = survey_data.get('Table 19')
        c_yield_major_crops = round(average_yield[major])
        
        c_national = [c_yield_major_crops['Irish potato'][30],c_yield_major_crops['Sweet potato'][30],c_yield_major_crops['Beans'][30]]
       

        plot = go.Figure(data=[go.Bar(
                
                name = 'National',
                x = major,
                y = c_national,orientation='v',
                marker_color = 'blue',
                text=[(f'{i}Kg/Ha') for i in c_national],textposition='auto',textfont_size=20, 

                ),
                
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'{igihe} 2022 Average yield Of Major Crops At National Level.'),
                title_x=.26,
            # width=3000,
            height=500,yaxis=dict( title='Kg/Ha', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Major Crops',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
    stl.subheader(":bar_chart: :green[Change In Major Crops production Per Season 2021 - 2022 At National Level]")
       
    if(igihe == 'Season A' or igihe ==None):
      
        # average yield
        crop_production = survey_data.get('Table 23')
        production = (crop_production[major])
        
        a_national_2022 = [round(production['Cassava'][30]),round(production['Bananas'][30]),round(production['Irish potato'][30]),round(production['Sweet potato'][30]),round(production['Paddy rice'][30]),round(production['Maize'][30]),round(production['Beans'][30])]
        a_national_2021 = [round(production['Cassava'][31]),round(production['Bananas'][31]),round(production['Irish potato'][31]),round(production['Sweet potato'][31]),round(production['Paddy rice'][31]),round(production['Maize'][31]),round(production['Beans'][31])]
        a_change = [round(production['Cassava'][32]*100,1),round(production['Bananas'][32]*100,1),round(production['Irish potato'][32]*100,1),round(production['Sweet potato'][32]*100,1),round(production['Paddy rice'][32]*100,1),round(production['Maize'][32]*100,1),round(production['Beans'][32]*100,1)]

        plot = go.Figure(data=[go.Bar(
                
                name = 'National 2022',
                y = major,
                x = a_national_2022,orientation='h',
                marker_color = 'blue',
                text=[(f'{i} MT') for i in a_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = a_national_2021,orientation='h',
                marker_color = 'green',
                text=[(f'{i} MT') for i in a_national_2021],textposition='outside',textfont_size=20, 


                ),
       
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'Season A Change In Production Of Main Crops 2022-2021'),
                title_x=.26,
            # width=300,
            height=600,yaxis=dict( title='Major Crops', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Metric Tones',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text('Major crops production in Season A')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{a_national_2022[major.index(i)]}] metric tones and :green[{a_national_2021[major.index(i)]}] metric tones in 2021 with a change of :red[{a_change[major.index(i)]}%]. ')

        
       

    if(igihe == 'Season B'):
         # average yield
        crop_production = survey_data.get('Table 24')
        production = (crop_production[major])
        
        b_national_2022 = [round(production['Cassava'][30]),round(production['Bananas'][30]),round(production['Irish potato'][30]),round(production['Sweet potato'][30]),round(production['Paddy rice'][30]),round(production['Maize'][30]),round(production['Beans'][30])]
        b_national_2021 = [round(production['Cassava'][31]),round(production['Bananas'][31]),round(production['Irish potato'][31]),round(production['Sweet potato'][31]),round(production['Paddy rice'][31]),round(production['Maize'][31]),round(production['Beans'][31])]
        b_change = [round(production['Cassava'][32]*100,1),round(production['Bananas'][32]*100,1),round(production['Irish potato'][32]*100,1),round(production['Sweet potato'][32]*100,1),round(production['Paddy rice'][32]*100,1),round(production['Maize'][32]*100,1),round(production['Beans'][32]*100,1)]

        plot = go.Figure(data=[go.Bar(
                
                name = 'National 2022',
                y = major,
                x = b_national_2022,orientation='h',
                marker_color = 'blue',
                text=[(f'{i} MT') for i in b_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = b_national_2021,orientation='h',
                marker_color = 'green',
                text=[(f'{i} MT') for i in b_national_2021],textposition='outside',textfont_size=20, 


                ),
       
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'{igihe} Change In Production Of Major Crops 2022-2021'),
                title_x=.26,
            # width=300,
            height=600,yaxis=dict( title='Major Crops', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Metric Tones',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text(f'Major crops production in {igihe}')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{b_national_2022[major.index(i)]}] metric tones and :green[{b_national_2021[major.index(i)]}] metric tones in 2021 with a change of :red[{b_change[major.index(i)]}%]. ')

    if(igihe == 'Season C'):
        # cultivated land
        crop_production = survey_data.get('Table 25')
        major = ['Irish potato','Sweet potato','Beans']
        production = crop_production[major]
        c_national_2022 = [round(production['Irish potato'][30]),round(production['Sweet potato'][30]),round(production['Beans'][30])]
        c_national_2021 = [round(production['Irish potato'][31]),round(production['Sweet potato'][31]),round(production['Beans'][31])]
        c_change = [round(production['Irish potato'][32]*100,1),round(production['Sweet potato'][32]*100,1),round(production['Beans'][32]*100,1)]

        plot = go.Figure(data=[go.Bar(
                
                name = 'National 2022',
                y = major,
                x = c_national_2022,orientation='h',
                marker_color = 'blue',
                text=[(f'{i} MT') for i in c_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = c_national_2021,orientation='h',
                marker_color = 'green',
                text=[(f'{i} MT') for i in c_national_2021],textposition='outside',textfont_size=20, 


                ),
       
            ])
        plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        plot.update_layout(
                title=(f'{igihe} Change In Production Of Major Crops 2022-2021'),
                title_x=.26,
            # width=300,
            height=600,yaxis=dict( title='Major Crops', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Metric Tones',titlefont_size=15,tickfont_size=14,),
            )
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text(f'Major crops production in {igihe}')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{c_national_2022[major.index(i)]}] metric tones and :green[{c_national_2021[major.index(i)]}] metric tones in 2021 with a change of :red[{c_change[major.index(i)]}%]. ')


        # plot = go.Figure(data=[go.Bar(
                
        #         name = 'National',
        #         x = major,
        #         y = c_national,orientation='v',
        #         marker_color = 'blue',
        #         text=[(f'{i}Kg/Ha') for i in c_national],textposition='auto',textfont_size=20, 

        #         ),
                
        #     ])
        # plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
        # plot.update_layout(
        #         title=(f'{igihe} 2022 Average yield Of Major Crops At National Level.'),
        #         title_x=.26,
        #     # width=3000,
        #     height=500,yaxis=dict( title='Kg/Ha', titlefont_size=15,tickfont_size=14,),
        #     xaxis=dict(title='Major Crops',titlefont_size=15,tickfont_size=14,),
        #     )
            
        # plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='orange', size=14))
        # stl.plotly_chart(plot,use_container_width=True)
    
