import pandas as pd
import numpy as np
import streamlit as stl
import plotly.express as px
import plotly.graph_objects as go

# reading the dataset
Labour_force = pd.read_excel('RLFS.xlsx',sheet_name=None)

def Know_this():
    
    stl.subheader(':bar_chart: How Population Were Employed In Agriculture Related Activities By Sex Per Province In 2022 ?')
    # kigali
    kigali_in_agriculture = Labour_force.get('Table 54')
    male_in_agriculture_kigali = kigali_in_agriculture[kigali_in_agriculture.columns[2]][3]
    female_in_agriculture_kigali = kigali_in_agriculture[kigali_in_agriculture.columns[3]][3]
    kigali_data = [male_in_agriculture_kigali,female_in_agriculture_kigali]
    # south province
    south_in_agriculture = Labour_force.get('Table 55')
    male_in_agriculture_south = south_in_agriculture[south_in_agriculture.columns[2]][3]
    female_in_agriculture_south = south_in_agriculture[south_in_agriculture.columns[3]][3]
    south_data = [male_in_agriculture_south,female_in_agriculture_south]

    
    
    # west province
    west_in_agriculture = Labour_force.get('Table 56')
    male_in_agriculture_west = west_in_agriculture[west_in_agriculture.columns[2]][3]
    female_in_agriculture_west = west_in_agriculture[west_in_agriculture.columns[3]][3]
    west_data = [male_in_agriculture_west,female_in_agriculture_west]

    
    # north province
    north_in_agriculture = Labour_force.get('Table 57')
    male_in_agriculture_north = north_in_agriculture[north_in_agriculture.columns[2]][4]
    female_in_agriculture_north = north_in_agriculture[north_in_agriculture.columns[3]][4]
    north_data = [male_in_agriculture_north,female_in_agriculture_north]

    # east province
    east_in_agriculture = Labour_force.get('Table 58')
    male_in_agriculture_east = east_in_agriculture[east_in_agriculture.columns[2]][4]
    female_in_agriculture_east = east_in_agriculture[east_in_agriculture.columns[3]][4]
    east_data = [male_in_agriculture_east,female_in_agriculture_east]
 
    total_male = male_in_agriculture_kigali +  male_in_agriculture_south + male_in_agriculture_north + male_in_agriculture_west + male_in_agriculture_east
    total_female = female_in_agriculture_kigali +  female_in_agriculture_south + female_in_agriculture_north + female_in_agriculture_west + female_in_agriculture_east
    males = male_in_agriculture_kigali +  male_in_agriculture_south + male_in_agriculture_north + male_in_agriculture_west + male_in_agriculture_east
    females = female_in_agriculture_kigali +  female_in_agriculture_south + female_in_agriculture_north + female_in_agriculture_west + female_in_agriculture_east
    total = total_female+total_male
    total = ('{:,}'.format(total))
    total_female = ("{:,}".format(total_female))
    total_male = ("{:,}".format(total_male))

    provinces = ['Kigali','South','West','North','East']
    
    fig = go.Figure(data=[go.Bar(
    
    name = 'Male',
    x = provinces,
    y = [male_in_agriculture_kigali,male_in_agriculture_south,male_in_agriculture_west,male_in_agriculture_north,male_in_agriculture_east],orientation='v',
    marker_color = '#00628e',
    text=[(f'{("{:,}".format(i))}') for i in [male_in_agriculture_kigali,male_in_agriculture_south,male_in_agriculture_west,male_in_agriculture_north,male_in_agriculture_east]],textposition='outside', 

    ),
    go.Bar(
    
    name = 'Female',
    x = provinces,
    y = [female_in_agriculture_kigali,female_in_agriculture_south,female_in_agriculture_west,female_in_agriculture_north,female_in_agriculture_east],orientation='v',
    marker_color = '#49abc8',
    text=[(f'{("{:,}".format(i))}') for i in [female_in_agriculture_kigali,female_in_agriculture_south,female_in_agriculture_west,female_in_agriculture_north,female_in_agriculture_east]],textposition='outside', 

    ),
    ])
    fig.update_layout(barmode='group', title=(f'People Employed In Agriculture, Forestry And Fishing By Sex') ,
                title_x=.26,
            width=3000,
            height=500,yaxis=dict( title='Number Of People', titlefont_size=15,tickfont_size=14,),
            xaxis=dict(title='Provinces',titlefont_size=15,tickfont_size=14,),)
    fig.update_xaxes(tickfont=dict(family='Rockwell', color='white', size=14))
    stl.plotly_chart(fig,use_container_width=True)
    
    # insights
    stl.write(f':heavy_check_mark: In Rwanda 2022, :orange[{total}] people over 16 years old were employed in agriculture, forestry and fishing, with :blue[{total_male}] Males and :violet[{total_female}] Females. The number show that except for South province where numbers for females are less than males but in other provinces numbers of females involved in agriculture, forestry and fishing are higher than males. This proves that More females were engaged in agriculture and other related activities.')
    
    #  migrants in agriculture related activities
    stl.subheader(':clipboard: what Was The Number Of Migrants Involved In Agriculture, Forestry And Fishing ?')
    migrant = Labour_force.get('Table 52')
    total_migrants_in_agriculture = migrant[migrant.columns[1]][3]
    ttl_migrants_in_agriculture = ("{:,}".format(total_migrants_in_agriculture))
    
    male_migrants_in_agriculture = migrant[migrant.columns[2]][3]
    male_migrants_in_agriculture = ("{:,}".format(male_migrants_in_agriculture))
    
    female_migrants_in_agriculture = migrant[migrant.columns[3]][3]
    female_migrants_in_agriculture = ("{:,}".format(female_migrants_in_agriculture))
    
    internal_migrants_in_agriculture = migrant[migrant.columns[6]][3]
    internal_migrants_in_agriculture = ("{:,}".format(internal_migrants_in_agriculture))
    
    external_migrants_in_agriculture = migrant[migrant.columns[7]][3]
    external_migrants_in_agriculture = ("{:,}".format(external_migrants_in_agriculture))
    
    ## drawing figue
    data = [(males+females)-total_migrants_in_agriculture,total_migrants_in_agriculture]
    Lables = ['Resident','Migrants']
    fig = px.pie(data, values=data, names=Lables)
    fig.update_traces(hoverinfo='percent+label', textinfo='percent')
    fig.update_layout(title_text="% of Migrants involved in agriculture, forestry and fishing",width=400, height=400,title_x=.2)
    stl.plotly_chart(fig,use_container_width=True)
    stl.write(f":ballot_box_with_check: In :orange[{total}] people who were invloved in agriculture, forestry and fishing in 2022,  :red[6.46%] were migrants equivalent to :blue[{ttl_migrants_in_agriculture}] people. :gray[{female_migrants_in_agriculture}] were female and :violet[{male_migrants_in_agriculture}] males. amonge them :green[{internal_migrants_in_agriculture}] were internal migrants and :blue[{external_migrants_in_agriculture}] were external migrants.")
    
    stl.subheader(f"	:timer_clock: what was average time spent in agriculture, forestry and fishing per sex in 2022 ?")
    stl.write(':ballot_box_with_check: On average males spent more time in agriculture,forestery and fishing as their main job than females. they spent :red[29.6] hours per week while females only spent :orange[27.5] hourse per week and this make on average a total of :green[28.5] hours per week.')
    stl.subheader(f":chart_with_downwards_trend: What was education level of population involved in agriculture, forestry and fishing and how does eduction level affected population's employment in agriculture and other related activities in 2022 ?")
    population_education_level  = Labour_force.get('Table 21')
    zero_level = population_education_level[population_education_level.columns[2]][3]
    primary = population_education_level[population_education_level.columns[3]][3]
    lower_secodary = population_education_level[population_education_level.columns[4]][3]
    upper_secondary = population_education_level[population_education_level.columns[5]][3]
    university = population_education_level[population_education_level.columns[6]][3]
    levels= ['None','Primary','Lower Secondary','Upper Secondary','University']


    data_value=[zero_level,primary,lower_secodary,upper_secondary,university]
    plt = px.bar(data_value,x=levels,y=data_value,color=levels,text=(data_value),title='Popilation In Agriculture And Their Level Of Education',range_y=[1000,2000000],
                 color_discrete_map = {"None":"#FF0000", "Primary":"#00FF00", "Lower Secondary":"#0000FF", "Upper Secondary":"#FFFF00", "University":"#800080"},labels = dict(y = "Population In Agriculture",x = "Level Of Education"))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    plt.update_traces(width=1)
    plt.update_layout(height=500,legend_title="Level Of Education",)
  
    plt.update_traces(textposition='outside')
    stl.plotly_chart(plt,use_container_width=True)
    stl.write(":ballot_box_with_check: More People Lose Interest In Agriculture, Forestry And Fishing As Their Level Of Eduction Increases. The Above Graph Shows That People With No Education Background Are More Involved In Agriculture, Forestry And Fishing.")
    
    
      

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    