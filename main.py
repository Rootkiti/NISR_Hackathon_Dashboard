import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
import agriculture_practices as ap
import crop_production_and_yield as cpy
import did_you_know as did
import streamlit as st
from streamlit_option_menu import option_menu


# reading data

survey_data = pd.read_excel("survey_data.xlsx", sheet_name=None)
location = pd.read_excel("provinces&district.xlsx", )
# labour_force = pd.read_excel('RLFS.xlsx', sheet_name=None)



# page configurating
stl.set_page_config( page_title="NISR 2023 Hackthon", page_icon=":bar_chart:", layout="wide" )
stl.title("SAS And RLFS Insights Presentation")

stl.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)



# sidebar
stl.sidebar.image('logo.png', use_column_width=None, clamp=False, channels="RGB", output_format="auto")
stl.sidebar.header("Choose Your Filter")
province = stl.sidebar.multiselect("Choose province",location["Province"].unique())

if not province:
    chosen_province = location.copy()
else:
    chosen_province =  location[location['Province'].isin(province)]  

#  selecting districts
dist = '' 

district = stl.sidebar.selectbox("Choose District",
   chosen_province["District"].unique().tolist(),
   index=None,
   placeholder="Select District...",)



if not district:
    pass
    # chosen_district = chosen_province.copy()
else:
    chosen_district =  location[location['District'] == district].reset_index(drop=True)
    dist = district.strip()
#  agriculture inputs
# what was major source for improved seed in each season in 2021 & 2022
source_of_improved_seed = survey_data.get('Table 5')
clr= ''

    
    

                   
# with tabs[1]:    
#     ap.showData(dist,seasons)
# with tabs[2]:
#     cpy.crop_production_yeald(survey_data,seasons) 
    
    
# with tabs[3]:
#     did.Know_this() 




# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 3

year = stl.sidebar.selectbox("Choose Year", [2021,2022])
seasons = stl.sidebar.selectbox("Choose Season", ['Season A','Season B','Season C'],index=None,placeholder="Select Seaason...")
colors = ['#00628e','#49abc8','#358a9a']
def streamlit_menu(example=3):

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Agriculture Inputs", "Agriculture Practices", "Land Use, Yield and Crops","Did You Know ?"],  # required
            icons=["h", "h", "h","h"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": '#13274F' },
                # "icon": {"color": "orange", "font-size": "15px"},
                "nav-link": {
                    "font-size": "17px",
                    "text-align": "left",
                    "margin": "3px",
                    "--hover-color": "#1F456E",
                },
                "nav-link-selected": {"background-color": '#0066B2'},
            },
        )
        return selected

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Agriculture Inputs":
    seeds_col, fertilizers_col = stl.columns(2)
    
    with seeds_col:
        table_columns = source_of_improved_seed.columns
        New_column_names = ['Source',	'Season A',	'Season B',	'Season C']
        
        # year of 2021

        seasonal_data_2021 = source_of_improved_seed[table_columns[0:4]].drop(0)
        seasonal_data_2021 = seasonal_data_2021.set_axis(New_column_names,axis=1)

        # stl.write(seasonal_data_2021)
        
        # year of 2022
        source = source_of_improved_seed[table_columns[0]]
        seasonal_data_2022 = pd.concat([source,source_of_improved_seed[table_columns[4:]]], axis=1).drop(0)
        seasonal_data_2022 = seasonal_data_2022.set_axis(New_column_names,axis=1)    
        
        if  year == 2021:
            annual_data = seasonal_data_2021.copy()
        else:
            annual_data =  seasonal_data_2022.copy()
            
        

        if not seasons:
            # anuual visualization of improved seeds source data
            filtered_data = annual_data.copy()
            stl.write(f'Source Of Improved Seeds And Quantity Provided In {year}')
            stl.bar_chart(filtered_data, x='Source', y= ['Season A','Season B','Season C'],color=colors)
            if(year == 2021):
                stl.write(f':pushpin: In 2021, major source of improved seeds was agro dealers, followed by NGOs/companies and the least supply was from other source')
            else:
                stl.write(f':pushpin: In 2022, major source of improved seeds was agro dealers, then NGOs/companies and the least supply was from other source')
            with stl.expander("View Visualized Data"):
                stl.write(filtered_data)
        else:
            # seasonal visualization of improved source data
           
            filtered_data =  pd.concat([source,annual_data[seasons]], axis=1).drop(0)

            stl.write(f'Source Of Improved Seeds And Quantity Provided In {year} {seasons}')
            stl.bar_chart(filtered_data, x='Source',)
            print(seasons)
            with stl.expander("View Visualized Data"):
               stl.write(filtered_data)

    
    with fertilizers_col:
        source_of_fertilizer = survey_data.get('Table 6')
        
        table_columns = source_of_fertilizer.columns
        New_column_names = ['Source',	'Season A',	'Season B',	'Season C']
        
        # year of 2021

        seasonal_fertilizers_data_2021 = source_of_fertilizer[table_columns[0:4]].drop(0)
        seasonal_fertilizers_data_2021 = seasonal_fertilizers_data_2021.set_axis(New_column_names,axis=1)

        
        # year of 2022
        source = source_of_fertilizer[table_columns[0]]
        seasonal_fertilizers_data_2022 = pd.concat([source,source_of_fertilizer[table_columns[4:]]], axis=1).drop(0)
        seasonal_fertilizers_data_2022 = seasonal_fertilizers_data_2022.set_axis(New_column_names,axis=1)
        
        if  year == 2021:
            fertilizer_annual_data = seasonal_fertilizers_data_2021.copy()
        else:
            fertilizer_annual_data =  seasonal_fertilizers_data_2022.copy()

        if not seasons:
            filtered_data = fertilizer_annual_data.copy()
            stl.write(f'Where Did Majority Of Farmers Buy inorganic Fertilizers In {year} ?')
            stl.bar_chart(filtered_data, x='Source', y= ['Season A','Season B','Season C'],color=colors)
            if(year == 2021):
                stl.write(f':pushpin: In 2021, most of farmers bought fertilizers from agro dealers, then NGOs/companies and the least bought from other source')
            else:
                stl.write(f':pushpin: In 2022, major of farmers bought fertilizers from agro dealers, followed by NGOs/companies and the least bought from other source')
            
            with stl.expander("View Visualized Data"):
                stl.write(filtered_data)
        else:
            filtered_data =  pd.concat([source,fertilizer_annual_data[seasons]], axis=1).drop(0)
            
            stl.write(f'Where Did Majority Of Farmers Buy inorganic Fertilizers In {year} {seasons}')
            stl.bar_chart(filtered_data, x='Source',)
            with stl.expander("View Visualized Data"):
                stl.write(filtered_data)
 
    # use of agriculture inputs  by farmers category

   
    new_column_names = ['District','Overall','SSF','LSF']


#**************************** adption to the use agbriculture inputs by farmes categoried section **********************************
    with stl.expander("What Is Seasonal % Of Adoption To The Use Of agriculture Inputs By Farmer Category In 2022"): 
        organic_in_season,inorganic_in_season,pesticides_in_season,seeds_in_season= stl.columns(4)
        season = stl.selectbox("Choose Season", ['Season A','Season B','Season C'])
        
        if  season =="Season A":
             improved_seeds_in_season = survey_data.get('Table 32')
             organic_fertilizer_in_season = survey_data.get('Table 38')
             inorganic_fertilizer_in_season = survey_data.get('Table 41')        
             pesticide_in_season = survey_data.get('Table 51')
             with organic_in_season:
                
                stl.write(":blue[Farmers who applied organic fertilizer]")
                column_names = organic_fertilizer_in_season.columns
                farmers_applied_organic = organic_fertilizer_in_season[column_names[0:4]]
                farmers_applied_organic = farmers_applied_organic.set_axis(new_column_names,axis=1)
                farmers_applied_organic = farmers_applied_organic.drop(0)
                notation = round(farmers_applied_organic['Overall'][31],1)
                data = [round(farmers_applied_organic['SSF'][31],1),(round(farmers_applied_organic['LSF'][31],1))]
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                a='a'
                fig.update_traces(textinfo=('value+label'),hoverinfo='name',textposition='inside', textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In season A of 2022, :green[{round(farmers_applied_organic['Overall'][31],1)}%] \nof farmers applied organic \nfertilizers with :blue[{round(farmers_applied_organic['SSF'][31],1)}%] of \nsmall-scale farmers and :red[{round(farmers_applied_organic['LSF'][31],1)}%] \nof large-scale farmers applied \norganic fertilizers.")
       
             with inorganic_in_season:
        
                stl.write(":blue[Farmers who used inorganic fertilizers]")
                cols = inorganic_fertilizer_in_season.columns
                farmers_applied_inorganic = inorganic_fertilizer_in_season[cols[0:4]]
                farmers_applied_inorganic = farmers_applied_inorganic.set_axis(new_column_names,axis=1)
                farmers_applied_inorganic = farmers_applied_inorganic.drop(0)
                data = [round(farmers_applied_inorganic['SSF'][31],1),(round(farmers_applied_inorganic['LSF'][31],1))]
                Lables = ['SSF (%)','LSF (%)']
                notation = round(farmers_applied_inorganic['Overall'][31],1)
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside', textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In season A of 2022, :red[{round(farmers_applied_inorganic['Overall'][31],1)}%] \nof farmers applied inorganic \nfertilizers with :blue[{round(farmers_applied_inorganic['SSF'][31],1)}%] of \nsmall-scale farmers and :green[{round(farmers_applied_inorganic['LSF'][31],1)}%] \nof large-scale farmers applied \ninorganic fertilizers.")

             with pesticides_in_season:
        
                stl.write(":blue[Farmers who used pesticides]")
                cols = pesticide_in_season.columns
                farmers_applied_pesticides = pesticide_in_season[cols[0:4]]
                farmers_applied_pesticides = farmers_applied_pesticides.set_axis(new_column_names,axis=1)
                farmers_applied_pesticides = farmers_applied_pesticides.drop(0)
                data = [round(farmers_applied_pesticides['SSF'][31],1),(round(farmers_applied_pesticides['LSF'][31],1))]
                notation = round(farmers_applied_pesticides['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
           
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In season A of 2022, :orange[{round(farmers_applied_pesticides['Overall'][31],1)}%] \nof farmers used pestsides with :blue[{round(farmers_applied_pesticides['SSF'][31],1)}%] of \nsmall-scale farmers and :green[{round(farmers_applied_pesticides['LSF'][31],1)}%] \nof large-scale farmers.")

                # rainbow
             with seeds_in_season:
        
                stl.write(":blue[Farmers who used improved seeds]")
                cols = improved_seeds_in_season.columns
                farmers_used_improved_seeds = improved_seeds_in_season[cols[0:4]]
                farmers_used_improved_seeds = farmers_used_improved_seeds.set_axis(new_column_names,axis=1,)
                farmers_used_improved_seeds = farmers_used_improved_seeds.drop(0)
                data = [round(farmers_used_improved_seeds['SSF'][31],1),(round(farmers_used_improved_seeds['LSF'][31],1))]

                notation = round(farmers_used_improved_seeds['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside', textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In {season} of 2022, :blue[{round(farmers_used_improved_seeds['Overall'][31],1)}%] \nof farmers used improved seeds with :rainbow[{round(farmers_used_improved_seeds['SSF'][31],1)}%] of \nsmall-scale farmers and :green[{round(farmers_used_improved_seeds['LSF'][31],1)}%] \nof large-scale farmers.")

              
        if  season == "Season B":
             improved_seeds_in_season = survey_data.get('Table 33')
             organic_fertilizer_in_season = survey_data.get('Table 39')
             inorganic_fertilizer_in_season = survey_data.get('Table 42')        
             pesticide_in_season = survey_data.get('Table 52')
             with organic_in_season:
                
                stl.write(":blue[farmers who applied organic fertilizer]")
                column_names = organic_fertilizer_in_season.columns
                farmers_applied_organic = organic_fertilizer_in_season[column_names[0:4]]
                farmers_applied_organic = farmers_applied_organic.set_axis(new_column_names,axis=1)
                farmers_applied_organic = farmers_applied_organic.drop(0)
                notation = round(farmers_applied_organic['Overall'][31],1)
                data = [round(farmers_applied_organic['SSF'][31],1),(round(farmers_applied_organic['LSF'][31],1))]
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
                 color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In {season} of 2022, :green[{round(farmers_applied_organic['Overall'][31],1)}%] \nof farmers applied organic \nfertilizers with a decrease of :red[11.8%] compared to season A.  :blue[{round(farmers_applied_organic['SSF'][31],1)}%] were \nsmall-scale farmers and :red[{round(farmers_applied_organic['LSF'][31],1)}%] \nof large-scale farmers.")
       
             with inorganic_in_season:
        
                stl.write(":blue[farmers who used inorganic fertilizers]")
                cols = inorganic_fertilizer_in_season.columns
                farmers_applied_inorganic = inorganic_fertilizer_in_season[cols[0:4]]
                farmers_applied_inorganic = farmers_applied_inorganic.set_axis(new_column_names,axis=1)
                farmers_applied_inorganic = farmers_applied_inorganic.drop(0)
                data = [round(farmers_applied_inorganic['SSF'][31],1),(round(farmers_applied_inorganic['LSF'][31],1))]
                Lables = ['SSF (%)','LSF (%)']
                notation = round(farmers_applied_inorganic['Overall'][31],1)
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f":red[{round(farmers_applied_inorganic['Overall'][31],1)}%] \nof farmers applied inorganic \nfertilizers In {season} of 2022, and decreased by :rainbow[11.1%] compared to season A. :blue[{round(farmers_applied_inorganic['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_applied_inorganic['LSF'][31],1)}%] \nof large-scale farmers.")

             with pesticides_in_season:
        
                stl.write(":blue[farmers who used pesticides]")
                cols = pesticide_in_season.columns
                farmers_applied_pesticides = pesticide_in_season[cols[0:4]]
                farmers_applied_pesticides = farmers_applied_pesticides.set_axis(new_column_names,axis=1)
                farmers_applied_pesticides = farmers_applied_pesticides.drop(0)
                data = [round(farmers_applied_pesticides['SSF'][31],1),(round(farmers_applied_pesticides['LSF'][31],1))]
                notation = round(farmers_applied_pesticides['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f":orange[{round(farmers_applied_pesticides['Overall'][31],1)}%] \nof farmers used pestsides and there was a decrease of :red[3.9%] compared to season A. :blue[{round(farmers_applied_pesticides['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_applied_pesticides['LSF'][31],1)}%] \nof large-scale farmers.")

             with seeds_in_season:
        
                stl.write(":blue[farmers who used improved seeds]")
                cols = improved_seeds_in_season.columns
                farmers_used_improved_seeds = improved_seeds_in_season[cols[0:4]]
                farmers_used_improved_seeds = farmers_used_improved_seeds.set_axis(new_column_names,axis=1)
                farmers_used_improved_seeds = farmers_used_improved_seeds.drop(0)
                data = [round(farmers_used_improved_seeds['SSF'][31],1),(round(farmers_used_improved_seeds['LSF'][31],1))]

                notation = round(farmers_used_improved_seeds['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In {season} of 2022, :blue[{round(farmers_used_improved_seeds['Overall'][31],1)}%] \nof farmers used improved seeds with a decrease of :red[24.4%] compared to season A. :rainbow[{round(farmers_used_improved_seeds['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_used_improved_seeds['LSF'][31],1)}%] \nlarge-scale farmers.")

        if season == "Season C":
             improved_seeds_in_season = survey_data.get('Table 34')
             organic_fertilizer_in_season = survey_data.get('Table 40')
             inorganic_fertilizer_in_season = survey_data.get('Table 43')        
             pesticide_in_season = survey_data.get('Table 53')
             with organic_in_season:
                
                stl.write(":blue[farmers who applied organic fertilizers]")
                column_names = organic_fertilizer_in_season.columns
                farmers_applied_organic = organic_fertilizer_in_season[column_names[0:4]]
                farmers_applied_organic = farmers_applied_organic.set_axis(new_column_names,axis=1)
                farmers_applied_organic = farmers_applied_organic.drop(0)
                notation = round(farmers_applied_organic['Overall'][31],1)
                data = [round(farmers_applied_organic['SSF'][31],1),(round(farmers_applied_organic['LSF'][31],1))]
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In {season} of 2022, :green[{round(farmers_applied_organic['Overall'][31],1)}%] \nof farmers applied organic \nfertilizers with an increase of :red[24.4%] compared to season B.  :blue[{round(farmers_applied_organic['SSF'][31],1)}%] were \nsmall-scale farmers and :red[{round(farmers_applied_organic['LSF'][31],1)}%] \nof large-scale farmers.")
       
             with inorganic_in_season:        
                stl.write(":blue[Farmers who used inorganic fertilizers]")
                cols = inorganic_fertilizer_in_season.columns
                farmers_applied_inorganic = inorganic_fertilizer_in_season[cols[0:4]]
                farmers_applied_inorganic = farmers_applied_inorganic.set_axis(new_column_names,axis=1)
                farmers_applied_inorganic = farmers_applied_inorganic.drop(0)
                data = [round(farmers_applied_inorganic['SSF'][31],1),(round(farmers_applied_inorganic['LSF'][31],1))]
                Lables = ['SSF(%)','LSF (%)']
                notation = round(farmers_applied_inorganic['Overall'][31],1)
                fig = px.pie(data, names=Lables,values=data, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f":red[{round(farmers_applied_inorganic['Overall'][31],1)}%] \nof farmers applied inorganic \nfertilizers In {season} of 2022, and increased by :rainbow[44%] compared to season B. :blue[{round(farmers_applied_inorganic['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_applied_inorganic['LSF'][31],1)}%] \nof large-scale farmers.")

             with pesticides_in_season:
        
                stl.write(":blue[Farmers who used pesticides]")
                cols = pesticide_in_season.columns
                farmers_applied_pesticides = pesticide_in_season[cols[0:4]]
                farmers_applied_pesticides = farmers_applied_pesticides.set_axis(new_column_names,axis=1)
                farmers_applied_pesticides = farmers_applied_pesticides.drop(0)
                data = [round(farmers_applied_pesticides['SSF'][31],1),(round(farmers_applied_pesticides['LSF'][31],1))]
                notation = round(farmers_applied_pesticides['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f":orange[{round(farmers_applied_pesticides['Overall'][31],1)}%] \nof farmers used pestsides in {season} and there was an increase of :red[54.2%] compared to season B. :blue[{round(farmers_applied_pesticides['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_applied_pesticides['LSF'][31],1)}%] \nof large-scale farmers.")

             with seeds_in_season:
        
                stl.write(":blue[Farmers who used improved seeds]")
                cols = improved_seeds_in_season.columns
                farmers_used_improved_seeds = improved_seeds_in_season[cols[0:4]]
                farmers_used_improved_seeds = farmers_used_improved_seeds.set_axis(new_column_names,axis=1)
                farmers_used_improved_seeds = farmers_used_improved_seeds.drop(0)
                data = [round(farmers_used_improved_seeds['SSF'][31],1),(round(farmers_used_improved_seeds['LSF'][31],1))]

                notation = round(farmers_used_improved_seeds['Overall'][31],1)
                Lables = ['SSF (%)','LSF (%)']
                fig = px.pie(data, values=data, names=Lables, hole=0.5,color = ['p1', 'p2'],
             color_discrete_map = {'p1': '#49abc8',
                                        'p2': '#00628e',
                                        })
                fig.update_traces(textinfo='value+label',hoverinfo='name',textposition='inside',textfont_size=16)
                fig.update_layout(width=250, height=250,annotations=[dict(text=(f'{notation}%'), x=0.5, y=0.5, font_size=15, showarrow=False)])
                stl.plotly_chart(fig,use_container_width=True)
                stl.write(f"In {season} of 2022, :blue[{round(farmers_used_improved_seeds['Overall'][31],1)}%] \nof farmers used improved seeds with an increase of :red[17.4%] compared to season B. :rainbow[{round(farmers_used_improved_seeds['SSF'][31],1)}%] were \nsmall-scale farmers and :green[{round(farmers_used_improved_seeds['LSF'][31],1)}%] \nlarge-scale farmers.")
if selected == "Agriculture Practices":
    ap.showData(dist,seasons)
if selected == "Land Use, Yield and Crops":
    cpy.crop_production_yeald(survey_data,seasons)
if selected == "Did You Know ?":
    did.Know_this()
