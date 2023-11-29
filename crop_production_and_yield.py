import pandas as pd
import numpy as np
import streamlit as stl
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from streamlit_folium import st_folium
import map_visual as mv






def crop_production_yeald(survey_data,igihe):
    
    # css
    
        
    visual = stl.radio('choose visual property',['Combined','Individual Crop'])
    trends = survey_data.get('Table 7')
    cols = trends.columns
    Years = cols[1:]
    color = ['yellow','bronze','#f6f2c5','#F5DEB3','cream','brown','red','green']
    # ******* cgross values change section *****************
    if(visual == 'Combined'):
        fig = go.Figure()
        for i in range(0,14):
            # fig.add_scatter(x=Years, y= trends.iloc[i,1:], name=trends['Crops '][i])
            fig.add_trace(go.Scatter(x=Years,y=trends.iloc[i,1:], name=trends['Crops '][i]    # this sets its legend entry
            ))


            fig.update_layout(
                xaxis_title="Years",
                yaxis_title="Gross Value (Value RWF per ha)",
                legend_title="Major Crops",
                title_text = "Change In Gross Value Of Major Crops From 2016 - 2022",
                title_x =0.3, title_y=.9
                
                
            )

        stl.plotly_chart(fig, use_container_width=True)
        
    else:
        individual_crop_fig = make_subplots(
        rows=5, cols=3,
        subplot_titles=('Maize','Sorghum','Paddy rice','Wheat','Cassava','Sweet potato','Irish potato','Cooking banana','Dessert banana','Banana for beer','Beans','Pea','Groundnut','Soybean','Overall GVA'))

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[0,1:],name=trends['Crops '][0]),
                    row=1, col=1)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[1,1:],name=trends['Crops '][1]),
                    row=1, col=2)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[2,1:],name=trends['Crops '][2]),
                    row=1, col=3)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[3,1:],name=trends['Crops '][3]),
                    row=2, col=1)
        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[4,1:],name=trends['Crops '][4]),
                    row=2, col=2)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[5,1:],name=trends['Crops '][5]),
                    row=2, col=3)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[6,1:],name=trends['Crops '][6]),
                    row=3, col=1)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[7,1:],name=trends['Crops '][7]),
                    row=3, col=2)
        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[8,1:],name=trends['Crops '][8]),
                    row=3, col=3)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[9,1:],name=trends['Crops '][9]),
                    row=4, col=1)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[10,1:],name=trends['Crops '][10]),
                    row=4, col=2)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[11,1:],name=trends['Crops '][11]),
                      row=4, col=3)
        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[12,1:],name=trends['Crops '][12]),
                    row=5, col=1)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[13,1:],name=trends['Crops '][13]),
                    row=5, col=2)

        individual_crop_fig.add_trace(go.Scatter(x=Years, y=trends.iloc[14,1:],name=trends['Crops '][14]),
                    row=5, col=3)

        layout = {
            "xaxis": {
                "title": "r",
            },
            "yaxis": {
                "title": r"$\psi$"
            },
            
            "xaxis2":{
                "title": "r"
            },
            "yaxis2": {
                "title": r"$\psi$"
            },
            
            "xaxis3":{
                "title": "r"
            }
        }                 

        individual_crop_fig.update_layout(height=800,
            title_text = "Change In Gross Value Of Major Crops From 2016 - 2022",
                        
            legend_title="Major Crops",
            title_x =0.3, title_y=1,
                        )

        stl.plotly_chart(individual_crop_fig, use_container_width=True)   
    
    stl.subheader(":bar_chart: What Was Overall Gross Value Per Year From 2016 To 2021 ?")
    
    
    #    # Your data
    overall_2016 = round(trends[cols[1]][14],0)
    overall_2019 = round(trends[cols[4]][14],0)
    overall_2017 = round(trends[cols[2]][14],0)
    overall_2020 = round(trends[cols[5]][14],0)
    overall_2018 = round(trends[cols[3]][14],0)
    overall_2021 = round(trends[cols[6]][14],0)

# Custom CSS for the card-like elements
    card_style = """
  <style>
        .card {
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 400px;
            padding: 20px;
            margin: 10px;
            width: 250px;
            height: 200px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            background-color: #000000;
        }
        .card h3 {
            font-size: 30px;
            margin-bottom: 10px;
        }
        .card p {
            margin: 5px 0;
            font-size: 16px;
            font-size: 20px;
        }

        .card-2016 {
            
            background-color: #49abc8; /* Yellow */
        }
        .card-2019 {
            background-color: #004969; /* orange */
        }
        .card-2017 {
            background-color: #266774; /* Green */
        }
        .card-2020 {
            background-color: #00628e; /* Blue */
        }
        .card-2018 {
            background-color: #358a9a; /* Pink */
        }
        .card-2021 {
            background-color: #4D818E; /* Lavender */
        }
    </style>
"""

    # Display the custom CSS
    st.markdown(card_style, unsafe_allow_html=True)

    # Creating layout using st.columns() for three columns
    col1, col2, col3 = st.columns(3)

    with col1:
       st.markdown('<div class="card card-2016"><h3>2016</h3><p>Overall GVA Increased</p><p><span style="font-size:28px;">&#8593;</span> {0} RWF per ha</p></div>'.format(overall_2016), unsafe_allow_html=True)
       st.markdown('<div class="card card-2019"><h3>2019</h3><p>Overall GVA Increased</p><p><span style="font-size:28px;">&#8593;</span>{0} RWF per ha</p></div>'.format(overall_2019), unsafe_allow_html=True)

    with col2:
       st.markdown('<div class="card card-2017"><h3>2017</h3><p>Overall GVA Increased</p><p><span style="font-size:28px;">&#8593;</span> {0} RWF per ha</p></div>'.format(overall_2017), unsafe_allow_html=True)
       st.markdown('<div class="card card-2020"><h3>2020</h3><p>Overall GVA Increased</p><p><span style="font-size:28px;">&#8593;</span> {0} RWF per ha</p></div>'.format(overall_2020), unsafe_allow_html=True)

    with col3:
       st.markdown('<div class="card card-2018"><h3>2018</h3><p>Overall GVA Increased</p><p><span style="font-size:28px;">&#8593;</span> {0} RWF per ha</p></div>'.format(overall_2018), unsafe_allow_html=True)
       st.markdown('<div class="card card-2021"><h3>2021</h3><p>Overall GVA Decreased</p><p><span style="font-size:28px;">&#8595;</span> {0} RWF per ha</p></div>'.format(overall_2021), unsafe_allow_html=True)


#    **************** change in agriculture lad section ***********************
    stl.subheader(":bar_chart: What was seasonal change in agriculture land and it's percentage per district in 2022 ?")

# choosing btn map and bar chart
    view_mode = stl.radio('Choose View Property',['Bar Chart','Map'])
    selection1,selection2 = stl.columns([3,.5])
    new_cols = ['District','Total land area','Agricultural land','percentage of agricultural land']

    with selection1:
        season_land_use = survey_data.get('Table 8')
        districts = season_land_use['District'][:30]
        selected_districts = stl.multiselect('select district',districts)
        
    with selection2:
        season = stl.radio('Select Season',['Season A','Season B'])
   
    if(view_mode == 'Bar Chart'):
       
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
                     marker_color = '#00628e',
                    text=[(f'{i}(1000 Ha)') for i in data_to_be_used['Total land area']],textposition='outside', 

                    ),
                    go.Bar(
                    name = 'Agricultural land',
                    x = selected_districts,
                    y = data_to_be_used['Agricultural land'],orientation='v',
                    marker_color = '#49abc8',
                    text=[(f'{i}(1000 Ha)') for i in data_to_be_used['Agricultural land']],textposition='outside', 


                    ),
         
                ])
                plot.update_traces(width=.5, marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
                plot.update_layout(
                    title=(f'{season} 2022 Agricultural land in {dist} (,1000 Ha)') ,
                    title_x=.26,
                width=200,
                height=500,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
                xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,), barmode='overlay'
                )
                
                plot.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
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
                marker_color = '#00628e',
                text=[(f'{i} (1000 Ha)') for i in data_to_be_used['Total land area']],textposition='outside', 

                ),
                go.Bar(
                name = 'Agricultural land',
                x = selected_districts,
                y = data_to_be_used['Agricultural land'],orientation='v',
                marker_color = '#49abc8',
                text=[(f'{i} (1000 Ha)') for i in data_to_be_used['Agricultural land']],textposition='outside', 


                    ),

            ])
            plot.update_traces(width=.3, marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
            plot.update_layout(
                title=(f'{season} 2022 Agricultural land in {dist} (,1000 Ha)'),
                title_x=.26,
            width=3000,
            height=500,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),barmode='overlay'
            )
            
            plot.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
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
                    marker_color = '#00628e',
                    ),
                    go.Bar(
                    name = 'Agricultural land',
                    x = data_to_be_used['District'][:30].tolist(),
                    y = data_to_be_used['Agricultural land'],orientation='v',
                    marker_color = '#49abc8',

                        ),

                ])
                plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
                plot.update_layout(
                    title=(f'{season} 2022 Agricultural land use per district (,1000 Ha)'),
                    title_x=.26,
                # width=3000,
                height=400,yaxis=dict( title='Land use per district (,1000 Ha)', titlefont_size=15,tickfont_size=14,),
                xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),
                )
                
                plot.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='white', size=14))
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
                    marker_color = '#00628e',
                    ),
                    go.Bar(
                    name = 'Agricultural land',
                    x = data_to_be_used['District'][:30].tolist(),
                    y = data_to_be_used['Agricultural land'],orientation='v',
                    marker_color = '#49abc8',

                        ),

                ])
                plot.update_traces(marker_line_color = 'pink', marker_line_width = .5, opacity = 1,)
                plot.update_layout(
                    title=(f'{season} 2022 Agricultural land use per district (1000 Ha)'),
                    title_x=.26,
                # width=3000,
                height=400,yaxis=dict( title='Land use per district (1000 Ha)', titlefont_size=15,tickfont_size=14,),
                xaxis=dict(title='Districts',titlefont_size=15,tickfont_size=14,),
                )
                
                plot.update_xaxes(tickangle=45, tickfont=dict(family='Rockwell', color='white', size=14))
                stl.plotly_chart(plot,use_container_width=True)
                stl.write(f' :ballot_box_with_check: Agricultural land Reduced From :green[1402.0(1000 Hecters)] In Season A To :blue[{data_to_be_used["Agricultural land"][30]}(1000 Hecters)] In Season B And \nCovered :orange[{data_to_be_used["percentage of agricultural land"][30]} %] Of total Area Land')
    
    # ***************************** map visualzation *************************************************
    else:
        stl.write('map')
        seasonal_data  = ''
        area_land = ''
        agri_land = ''
        if (season == 'Season A'):
            season_a_land_use = survey_data.get('Table 8')
            cols = season_a_land_use.columns
            data_to_be_used = round(season_a_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
            seasonal_data = data_to_be_used["Agricultural land"][30]
            
            area_land = data_to_be_used['Total land area']
            
            agri_land = data_to_be_used['Agricultural land']
           
        else:
            season_b_land_use = survey_data.get('Table 9')
            cols = season_b_land_use.columns
            data_to_be_used = round(season_b_land_use[cols[0:4]],1)
            data_to_be_used = data_to_be_used.set_axis(new_cols,axis=1)
        
            area_land = data_to_be_used['Total land area']           
            agri_land = data_to_be_used['Agricultural land']
              
            
        map = mv.draw_map(area_land,agri_land)
        st_folium(map, width=1000)
        
    
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
                marker_color = '#358a9a',
                text=[(f'{i}Kg/Ha') for i in a_national],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'Small Scale farmers',
                y = major,
                x = a_ssf,orientation='h',
                marker_color = '#49abc8',
                text=[(f'{i}Kg/Ha') for i in a_ssf],textposition='outside',textfont_size=20, 


                ),
                go.Bar(
                name = 'Larger scale Farmers',
                y = major,
                x = a_lsf,orientation='h',
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='White', size=14))
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
                marker_color = '#358a9a',
                text=[(f'{i}Kg/Ha') for i in b_national],textposition='outside',textfont_size=20, 

                ),
                go.Bar(
                name = 'Small Scale farmers',
                y = major,
                x = b_ssf,orientation='h',
                marker_color = '#49abc8',
                text=[(f'{i}Kg/Ha') for i in b_ssf],textposition='outside',textfont_size=20, 


                ),
                go.Bar(
                name = 'Larger scale Farmers',
                y = major,
                x = b_lsf,orientation='h',
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='white', size=14))
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
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='white', size=14))
        stl.plotly_chart(plot,use_container_width=True)
    stl.subheader(":bar_chart: Change In Major Crops production Per Season 2021 - 2022 At National Level")
       
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
                
                marker_color = '#49abc8',
                text=[(f'{i} MT') for i in a_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = a_national_2021,orientation='h',
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='white', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text('Major crops production in Season A')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{a_national_2022[major.index(i)]}] metric tones and :green[{a_national_2021[major.index(i)]}] metric tones in 2021 with a change of :orange[{a_change[major.index(i)]}%]. ')
   

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
                marker_color = '#49abc8',
                text=[(f'{i} MT') for i in b_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = b_national_2021,orientation='h',
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='white', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text(f'Major crops production in {igihe}')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{b_national_2022[major.index(i)]}] metric tones and :green[{b_national_2021[major.index(i)]}] metric tones in 2021 with a change of :orange[{b_change[major.index(i)]}%]. ')

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
                marker_color = '#49abc8',
                text=[(f'{i} MT') for i in c_national_2022],textposition='outside',textfont_size=15, 

                ),
                go.Bar(
                name = 'National 2021',
                y = major,
                x = c_national_2021,orientation='h',
                marker_color = '#00628e',
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
            
        plot.update_xaxes(tickangle=0, tickfont=dict(family='Rockwell', color='white', size=14))
        stl.plotly_chart(plot,use_container_width=True)
        # mesaage
        stl.text(f'Major crops production in {igihe}')
        for i in major:
            
            stl.write(f':pushpin: In 2022, {i} production was :blue[{c_national_2022[major.index(i)]}] metric tones and :green[{c_national_2021[major.index(i)]}] metric tones in 2021 with a change of :orange[{c_change[major.index(i)]}%]. ')


    
