import pandas as pd
import streamlit as st
import base64
from catboost import CatBoostClassifier
from PIL import Image
from sklearn.preprocessing import MinMaxScaler
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit_elements import elements, mui, nivo
from streamlit_echarts import st_echarts 

st.set_page_config(
    page_title="Premier League 2022/23",
    layout='wide'
)

def enter():
    st.markdown("<br>", unsafe_allow_html=True)
def horizontal_line():
    st.markdown("<hr>", unsafe_allow_html=True)
def logo_link(link, path_img, width):
    st.markdown(
        """<div style="display: grid; place-items: center;">
        <a href="{}">
        <img src="data:image/png;base64,{}" width="{}">
        </a></div>""".format(
            link,
            base64.b64encode(open(path_img, "rb").read()).decode(),
            width,
        ),
        unsafe_allow_html=True,
    )    

with st.sidebar:
    st.markdown("""
        <div style='text-align: center; font-size:24px'>
            <b>
            Premeir League <br> 2022/2023 <br>
            </b>
        </div>
    """, unsafe_allow_html=True)
    
    enter()
    
    logo_link('', r'Images/premier-league-icon.png', 125)

    horizontal_line()
    
    selected_option_menu = option_menu(menu_title=None, 
                    options=["Summary Information", 'Player Stats', 'Club Stats', 'Predict Season 2023/24 Match Result'], 
                    icons=['house'], 
                    menu_icon="cast", default_index=0
    )
    horizontal_line()
    
    st.markdown("""
        <div style='text-align: center; font-size:20px'>
            <b>Related Links</b> <br>
            <a href="https://www.premierleague.com" style="text-decoration: none;">Data Source</a> <br>
            <a href="https://github.com/TheOX027/Premier-League-2022-2023-Streamlit-App" style="text-decoration: none;">Github Repository</a> <br>
            <a href="https://www.linkedin.com/in/marselius-agus-dhion/" style="text-decoration: none;">Marselius Agus Dhion</a>
        </div>
    """, unsafe_allow_html=True)

if selected_option_menu == "Summary Information" : 
    paragraph_1 = "The Premier League season 2022/2023 has concluded and has provided some unexpected events. One of the surprising moments is when Arsenal managed to give a tough competition to Manchester City in the race for the English Premier League title. Arsenal secured the top spot in the Premier League table for 29 weeks. However, Arsenal failed to maintain their consistency until the end of the season, partly due to injuries to key players and Manchester City's consistent performance when Arsenal was not performing well. In the end, Manchester City secured the first position until the last gameweek. Another surprise came from Eddie Howe's team, Newcastle United. The last time Newcastle entered the top four was in the 2003/2004 season when Alan Shearer captained the team, and they ultimately secured the fourth position. Additionally, Manchester United also secured their spot in the Champions League."
    paragraph_2 = "Apart from Manchester City, Arsenal, and Newcastle City, who secured places in the Champions League for the next season, there are four other teams that earned spots to play outside the Premier League. Liverpool and Brighton & Hove Albion claimed the fifth and sixth positions, respectively, earning spots in the Europa League. Aston Villa secured the seventh position, allowing them to play in the Conference League next season. The last team to surprisingly earn a spot in the Europa League is West Ham. West Ham earned their place in the Europa League by winning the Conference League, defeating Fiorentina with a score of 2-1."
    paragraph_3 = "In addition to the eight teams that successfully played in European competitions, two teams, Tottenham and Chelsea, did not perform well this season. Tottenham consistently held a top-four position at the beginning of the season. Meanwhile, Chelsea, despite investing heavily, had a poor performance, partly due to the large number of players, leading to a lack of a definite lineup for the team."
    paragrah_4 = "Every season, three teams experience relegation. This season, the relegated teams are the Premier League champions of the 2015/2016 season, Leicester City, Leeds United, and Southampton. In the 38th gameweek or the last match, four teams were at risk of relegation, with Everton being one of them. Everton avoided relegation by winning against Bournemouth with a score of 1-0, even though Leicester won their match against West Ham with a final score of 2-1. However, Leicester was ultimately relegated. In the last gameweek, Southampton also had an interesting match, drawing against Liverpool with a significant score of 4-4."
    
    justify_text = """
        <style>
        .text-justify {
            text-align: justify;
            text-justify: inter-word;
            font-size: 16px;
        }
        </style>
    """

    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b>
            Premier League 2022/23 Overview
            </b>
        </div>
    """, unsafe_allow_html=True) 
    horizontal_line()
    
    enter()
    
    # Club posisi ke-1,2,3,4
    col_1_1, col_1_2 = st.columns([3,1])
    with col_1_1 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{paragraph_1}</div>', unsafe_allow_html=True)
    with col_1_2 :
        man_city_img = Image.open('Images/man-city.jpeg')
        st.image(man_city_img, caption='Man City Players Lifting PL Trophy',  use_column_width=True)
    
    # Club posisi ke-5,6,7, dan West Ham
    col_2_1, col_2_2 = st.columns([1,3])
    with col_2_1 : 
        west_ham_img = Image.open('Images/west-ham-conf-league.jpeg')
        st.image(west_ham_img, caption='Declan Rice with Conference League Trophy', use_column_width=True)
    with col_2_2 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{paragraph_2}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{paragraph_3}</div>', unsafe_allow_html=True)
       
    col_3_1, col_3_2 = st.columns([3,1])
    with col_3_1 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{paragrah_4}</div>', unsafe_allow_html=True)
    with col_3_2 :
        lei_city_img = Image.open('Images/lei-relegated.jpg')
        st.image(lei_city_img, caption='Leicester City players after getting relegated', use_column_width=True)
    
    horizontal_line()

    # Membaca file CSV
    data = pd.read_csv('Established Datasets/Position per Gameweek.csv')
    pl_standings = pd.read_csv('Established Datasets/PL 22-23 Standings.csv', index_col=0)

    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b> Final Standings </b>
        </div>
    """, unsafe_allow_html=True) 
    horizontal_line()

    enter()    
    
    # Fungsi untuk memberikan warna pada baris
    def highlight_row(row):
        if row.name in [1, 2, 3, 4]:
            return ['background-color: #2940D3'] * len(row)  # Light blue
        elif row.name in [5, 6]:
            return ['background-color: #DC5F00'] * len(row)  # Light orange
        elif row.name == 7:
            return ['background-color: #1C7947'] * len(row)  # Light green
        elif row.name >= 18:
            return ['background-color: #CF0A0A'] * len(row)  # Light red
        else:
            return [''] * len(row)
        
    # Menampilkan DataFrame dengan warna pada baris
    st.dataframe(pl_standings.drop('Image_club', axis=1).style.apply(highlight_row, axis=1), use_container_width=True)

    legend = {
        'Label': ['Champions League', 'Europa League', 'Conference League', 'Relegation'],
        'Warna': ['#2940D3', '#DC5F00', '#1C7947', '#CF0A0A']
    }

    df_legend = pd.DataFrame(legend)

    st.subheader('Legend')
    legenda_html = ""
    for i in range(len(df_legend)):
        label = df_legend.loc[i, 'Label']
        color = df_legend.loc[i, 'Warna']
        legenda_html += f'<span style="color:{color}">■</span> {label} &nbsp;&nbsp;'

    st.markdown(f'<div style="white-space: nowrap;">{legenda_html}</div>', unsafe_allow_html=True)
    enter()
    
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b> Performance Chart </b>
        </div>
    """, unsafe_allow_html=True) 
    horizontal_line()

    # Filter klub
    clubs = data['Club'].unique()
    selected_clubs = st.multiselect('Choose Club (One or More Than One Club)', clubs)
    selected_data = data[data['Club'].isin(selected_clubs)]

    # Tambahkan kode ECharts di sini
    option = {
        "title": {"text": "Position"},
        "tooltip": {"trigger": "item", "formatter": "Position: {c}"},
        "legend": {"data": selected_clubs, "show": True, "textStyle": {"color": "white"}},
        "grid": {"left": 30, "right": 110, "bottom": 30, "containLabel": True},
        "xAxis": {
            "type": "category",
            "name": "Gameweek",
            "splitLine": {"show": True},
            "axisLabel": {"margin": 10, "fontSize": 12},
            "boundaryGap": False,
            "data": selected_data['Gameweek'].unique().tolist()
        },
        "yAxis": {
            "type": "value",
            "axisLabel": {"margin": 30, "fontSize": 12, "formatter": '{value}'},
            "inverse": True,
            "interval": 1,
            "min": 1,
            "max": 20
        },
        "series": [
            {
                "name": club,
                "symbolSize": 10,
                "type": 'line',
                "smooth": True,
                "emphasis": {"focus": 'series'},
                "endLabel": {"show": True, "formatter": '{a}', "distance": 20, "color": "white"},
                "lineStyle": {"width": 3},
                "data": selected_data[selected_data['Club'] == club]['Position'].tolist()
            }
            for club in selected_clubs
        ]
    }

    # Tampilkan grafik menggunakan st_echarts
    st_echarts(options=option, height="500px")


if selected_option_menu == "Player Stats" : 
    st.markdown(
        """
        <style>
        .text-right {
            text-align: right;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    col_scorer_header, _ = st.columns([2,1])
    with col_scorer_header:
        colored_header(
            label="Top Scorer",
            description="",
            color_name="orange-70",
        )
    
    col_scorer, col_scorer_img = st.columns([2,1])
    enter()
    
    _, col_assist_header = st.columns([1,2])
    with col_assist_header:
        colored_header(
            label="Top Assist",
            description="",
            color_name="orange-70",
        )

    col_assist_img, col_assist = st.columns([1,2])
    enter()

    col_clean_sheet_header, _ = st.columns([2,1])
    with col_clean_sheet_header:
        colored_header(
            label="Top Clean Sheet",
            description="",
            color_name="orange-70",
        )
        
    col_cleansheet, col_cleansheet_img = st.columns([2,1])
    enter()

    with st.container(): 
        with col_scorer :
            df_top_scorer = pd.read_csv('Established Datasets/Top Scorers.csv', index_col=0)
            st.dataframe(df_top_scorer, use_container_width=True)
                    
        with col_scorer_img :
            golden_boot_img = Image.open('Images/golden-boot.jpg')
            st.image(golden_boot_img, caption='Erling Braut Halaand')
            
            with st.expander('Player Features Stats') : 
                feature_names = ['Headed Goals', 'Goals with right foot', 'Goals with left foot', 'Penalties Scored', 'Shots accuracy (%)', 'Big chances missed']
                feature_values = [7, 6, 23, 7, 49, 28]
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
                radar_data = [{"indicator": {"text": feature, "itemStyle": {"color": "#FFFFFF"}}, "value": value} for feature, value in zip(feature_names, feature_values) if feature in selected_features]

                with elements(f"nivo_charts_top_scorer"):
                    with mui.Box(sx={"height": 400}):
                        nivo.Radar(
                            data=radar_data,
                            keys=["value"],
                            indexBy="indicator.text",
                            margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                            theme={"background": "#0E1117", "tooltip": {"container": {"background": "#0E1117", "color": "#FFFFFF"}}},   
                        )
                
        with col_assist :
            df_top_assist = pd.read_csv('Established Datasets/Top Asissts.csv', index_col=0)
            st.dataframe(df_top_assist, use_container_width=True)
            
        with col_assist_img : 
            pots_img = Image.open('Images/playmaker-of-the-season.jpg')
            st.image(pots_img, caption='Kevin de Bruyne', use_column_width=True)
            with st.expander('Player Features Stats') :

                feature_names = ['Passes per match', 'Big chances created', 'Cross accuracy (%)', 'Through balls', 'Accurate long balls']
                feature_values = [42.41, 31, 29, 28, 81]
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
                radar_data = [{"indicator": {"text": feature, "itemStyle": {"color": "#FFFFFF"}}, "value": value} for feature, value in zip(feature_names, feature_values) if feature in selected_features]

                with elements(f"nivo_charts_top_assist"):
                    with mui.Box(sx={"height": 400}):
                        nivo.Radar(
                            data=radar_data,
                            keys=["value"],
                            indexBy="indicator.text",
                            margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                            theme={"background": "#0E1117", "tooltip": {"container": {"background": "#0E1117", "color": "#FFFFFF"}}},   
                        )
        
                                                        
        with col_cleansheet :
            df_top_cleansheet = pd.read_csv('Established Datasets/Top Clean Sheet.csv', index_col=0)
            st.dataframe(df_top_cleansheet, use_container_width=True)
            
        with col_cleansheet_img:
            golden_glove_img = Image.open('Images/golden-glove.jpg')
            st.image(golden_glove_img, caption='David de Gea')
            with st.expander('Player Features Stats') :
                feature_names = ['Saves', 'Penalties Saved', 'Goal Conceded', 'Erros leading to goal', 'Own goals', 'Accurate long balls', 'Punches', 'High Claims', 'Catches']
                feature_values = [101, 1, 43, 2, 0, 187, 12, 14, 5]
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
            
                with elements(f"nivo_charts_clean_sheet"):
                    with mui.Box(sx={"height": 400}):
                        nivo.Radar(
                            data=radar_data,
                            keys=["value"],
                            indexBy="indicator.text",
                            margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                            theme={"background": "#0E1117", "tooltip": {"container": {"background": "#0E1117", "color": "#FFFFFF"}}},   
                        )                        
                        
    
if selected_option_menu == "Club Stats" : 
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b> Club Attribute Stats </b>
        </div>
    """, unsafe_allow_html=True)
    horizontal_line()
    
    def radar_chart_attr(data, default_attr, key):
        data['Club'] = data['Club'].str.strip()
        selected_clubs = st.multiselect(
            "Select Clubs", 
            options=data["Club"].unique(), 
            default=['Arsenal', 'Manchester City', 'Southampton'],
            key=f"club_{key}"
        )
        selected_columns = st.multiselect(
            "Select Attribute", 
            options=data.columns[2:], 
            default=default_attr,
            key=f"attr_{key}"
        )

        filtered_data = data[data["Club"].isin(selected_clubs)]

        # Prepare data for radar chart
        radar_data = []
        for _, row in filtered_data.iterrows():
            radar_data.append({"Club": row["Club"], **{col: row[col] for col in selected_columns}})

        max_value = max(filtered_data[selected_columns].max())

        # Render radar chart
        with elements(f"nivo_charts_{key}"):
            with mui.Box(sx={"height": 400}):
                nivo.Radar(
                    data=radar_data,
                    keys=selected_columns,
                    indexBy="Club",
                    valueFormat=">-.2f",
                    margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                    borderColor={"from": "color"},
                    gridLabelOffset=36,
                    dotSize=10,
                    dotColor={"theme": "background"},
                    dotBorderWidth=2,
                    # maxValue=max_value + 20,
                    motionConfig="wobbly",
                    legends=[
                        {
                            "anchor": "top-left",
                            "direction": "column",
                            "translateX": -50,
                            "translateY": -40,
                            "itemHeight": 20,
                            "itemTextColor": "#FFFFFF",
                            "symbolSize": 12,
                            "itemTextSize": 14,
                            "symbolShape": "circle",
                            "effects": [
                                {
                                    "on": "hover",
                                    "style": {
                                        "itemTextColor": "#999"
                                    }
                                }
                            ]
                        }
                    ],
                    theme={
                        "background": "#0E1117",
                        "textColor": "#FFFFFF",
                        "tooltip": {
                            "container": {
                                "background": "#0E1117",
                                "color": "#FFFFFF",
                            }
                        }
                    },
                )

    att_col, def_col, teamplay_col = st.columns(3)

    with att_col:
        st.markdown("""
            <div style='text-align: center; font-size:32px'>
                <b> Attack Attributes </b>
            </div>
        """, unsafe_allow_html=True)
        enter()
        with st.expander('Choose Club Here', expanded=True):
            df_attack = pd.read_csv('Established Datasets/attack.csv')
            radar_chart_attr(df_attack, default_attr=["Goals Inside Box", "Goals Outside Box"], key="attack")

    with def_col:
        st.markdown("""
            <div style='text-align: center; font-size:32px'>
                <b> Defence Attributes </b>
            </div>
        """, unsafe_allow_html=True)
        enter()
        with st.expander('Choose Club Here', expanded=True):
            df_defence = pd.read_csv('Established Datasets/defence.csv')
            radar_chart_attr(df_defence, default_attr=["Penalties Conceded", "Clean Sheets"], key="defence")

    with teamplay_col:
        st.markdown("""
            <div style='text-align: center; font-size:32px'>
                <b> Team Play Attributes </b>
            </div>
        """, unsafe_allow_html=True)
        enter()
        with st.expander('Choose Club Here', expanded=True):
            df_team_play = pd.read_csv('Established Datasets/team_play.csv')
            radar_chart_attr(df_team_play, default_attr=["Crosses", "Through Ball"], key="team_play")
                                            
if selected_option_menu == "Predict Season 2023/24 Match Result" : 
    horizontal_line()
    st.markdown("""
        <div style='text-align: center; font-size:32px'>
            <b>
            Predict Season 2023/24 Match Result
            </b>
        </div>
    """, unsafe_allow_html=True)
    horizontal_line()
    enter()
    
    # Initialize the scaler
    scaler = MinMaxScaler()
    scaler.fit(pd.DataFrame({
        'ht_home_score': [0, 5],
        'ht_away_score': [0, 5],
        'home_possession_%': [0.17, 0.82],
        'away_possession_%': [0.17, 0.82],
        'home_shots_on_target': [0, 17],
        'away_shots_on_target': [0, 15],
        'home_shots': [0, 44],
        'away_shots': [0, 33],
        'home_touches': [335, 1160],
        'away_touches': [294, 1116],
        'home_passes': [155, 1015],
        'away_passes': [148, 976],
        'home_tackles': [3, 48],
        'away_tackles': [3, 50],
        'home_clearances': [0, 107],
        'away_clearances': [1, 129],
        'home_corners': [0, 20],
        'away_corners': [0, 19],
        'home_offsides': [0, 14],
        'away_offsides': [0, 12],
        'home_yellow_cards': [0, 7],
        'away_yellow_cards': [0, 9],
        'home_red_cards': [0, 2],
        'away_red_cards': [0, 2],
        'home_fouls': [0, 34],
        'away_fouls': [0, 29],
        'home_total_points_last_5': [0, 15],
        'away_total_points_last_5': [0, 15],
        'home_h2h_points_last_5': [0, 15],
        'away_h2h_points_last_5': [0, 15],
    }))

    def preprocess_input(data):
        df = pd.DataFrame([data])
        numeric_features = ['ht_home_score', 'ht_away_score', 'home_possession_%',
        'away_possession_%', 'home_shots_on_target', 'away_shots_on_target',
        'home_shots', 'away_shots', 'home_touches', 'away_touches',
        'home_passes', 'away_passes', 'home_tackles', 'away_tackles',
        'home_clearances', 'away_clearances', 'home_corners', 'away_corners',
        'home_offsides', 'away_offsides', 'home_yellow_cards',
        'away_yellow_cards', 'home_red_cards', 'away_red_cards', 'home_fouls',
        'away_fouls', 'home_total_points_last_5', 'away_total_points_last_5',
        'home_h2h_points_last_5', 'away_h2h_points_last_5']
        
        df[numeric_features] = scaler.transform(df[numeric_features])
        return df

    # Mapping teams to numbers
    team_map = {
        "Arsenal": 0, "Aston Villa": 1, "Bournemouth": 6,
        "Brentford": 7, "Brighton & Hove Albion": 8,
        "Burnley": 9, "Chelsea": 12, "Crystal Palace": 13,
        "Everton": 15, "Fulham": 16, "Liverpool": 21,
        "Manchester City": 22, "Manchester United": 23,
        "Newcastle United": 26, "Nottingham Forest": 28,
        "Sheffield United": 32, "Tottenham Hostpur": 37,
        "West Ham United": 40, "Wolverhampton Wanderers": 42
    }

    # Derby teams list
    derby_teams = [
        ['Liverpool', 'Everton'],
        ['Arsenal', 'Tottenham'],
        ['Aston Villa', 'Birmingham City', 'Wolverhampton Wanderers'],
        ['Manchester United', 'Manchester City'],
        ['Newcastle United', 'Sunderland'],
        ['Portsmouth', 'Southampton'],
        ['Chelsea', 'Fulham', 'Queens Park Rangers'],
        ['Derby County', 'Leicester', 'Nottingham Forest'],
        ['Blackburn Rovers', 'Bolton Wanderers', 'Burnley', 'Blackpool'],
        ['Middlesbrough', 'Sunderland'],
        ['Stoke City', 'Port Vale'],
        ['Leeds United', 'Huddersfield Town'],
        ['Sheffield United', 'Sheffield Wednesday'],
        ['Norwich City', 'Ipswich Town'],
        ['Cardiff City', 'Swansea City'],
        ['Southampton', 'Portsmouth'],
        ['Bristol City', 'Bristol Rovers'],
        ['Nottingham Forest', 'Notts County']
    ]

    # Function to determine if the match is a derby
    def is_derby(home_team, away_team):
        for derby_pair in derby_teams:
            if home_team in derby_pair and away_team in derby_pair:
                return 1
        return 0

    cols_home_team, col_penengah, cols_away_team = st.columns([3, 2, 3])

    with cols_home_team:
        home_team_default_index = list(team_map.keys()).index("Arsenal")
        home_team = st.selectbox('Home Team', options=list(team_map.keys()), index=home_team_default_index)
        col_home_ht_score, col_possession_home = st.columns(2)
        
        with col_home_ht_score:
            ht_home_score = st.number_input('HT Home Scored', value=0)
        with col_possession_home:
            home_possession = st.slider('Home Team Possesion', 0, 100, value=0)
        
        st.write("____")
        
        cols_home_1, cols_home_2, cols_home_3, cols_home_4 = st.columns(4)
        
        with cols_home_1:
            home_shots_on_target = st.number_input('Shots on Target (H)', value=0)
            home_shots = st.number_input('Shots (H)', value=0)
            home_touches = st.number_input('Touches (H)', value=0)
        with cols_home_2:
            home_passes = st.number_input('Passes (H)', value=0)
            home_tackles = st.number_input('Tackles (H)', value=0)
            home_clearances = st.number_input('Clearances (H)', value=0)
        with cols_home_3:
            home_corners = st.number_input('Corners (H)', value=0)
            home_offsides = st.number_input('Offsides (H)', value=0)
            home_fouls = st.number_input('Fouls (H)', value=0)
        with cols_home_4:
            home_yellow_cards = st.number_input('Yellow Cards (H)', value=0)
            home_red_cards = st.number_input('Red Cards (H)', value=0)
        
        st.write("____")
        
        col_home_points_last_5, col_home_h2h_points_last_5 = st.columns(2)
        with col_home_points_last_5:
            home_total_points_last_5 = st.number_input('Total Points from Last 5 Games (H)', value=0)
        with col_home_h2h_points_last_5:
            home_h2h_points_last_5 = st.number_input('H2H Total Points from Last 5 Games (H)', value=0)

    with col_penengah:
        venue_dict = {
            'Arsenal': [11, 'Emirates Stadium, London'],
            'Aston Villa': [48, 'Villa Park, Birmingham'],
            'Bournemouth': [49, 'Vitality Stadium, Bournemouth'],
            'Brentford': [17, 'Gtech Community Stadium, Brentford'],
            'Burnley': [45, 'Turf Moor, Burnley'],
            'Chelsea': [39, 'Stamford Bridge, London'],
            'Crystal Palace': [32, 'Selhurst Park, London'],
            'Everton': [16, 'Goodison Park, Liverpool'],
            'Fulham': [8, 'Craven Cottage, London'],
            'Liverpool': [1, 'Anfield, Liverpool'],
            'Manchester City': [12, 'Etihad Stadium, Manchester'],
            'Manchester United': [29, 'Old Trafford, Manchester'],
            'Newcastle United': [36, "St. James' Park, Newcastle"],
            'Nottingham Forest': [40, 'The City Ground, Nottingham'],
            'Sheffield United': [4, 'Bramall Lane, Sheffield'],
            'Tottenham': [50, 'Wembley Stadium, London'],
            'West Ham': [24, 'London Stadium, London'],
            'Wolverhampton Wanderers': [28, 'Molineux Stadium, Wolverhampton'],
        }

        referee_map = {
            'Michael Oliver': 31, 'Andy Madley': 25,
            'Robert Jones': 11, 'Peter Bankes': 40,
            'Craig Pawson': 41, 'Jarred Gillett': 23,
            'Darren England': 21, 'Michael Salisbury': 39,
            'John Brooks': 42, 'Tony Harrington': 44,
            'David Coote': 47, 'Graham Scott': 27,
            'Thomas Bramall': 17, 'Chris Kavanagh': 35
        }

        venue_show = st.text_input('Venue/Stadium', value=venue_dict[home_team][1], disabled=True)
        venue = venue_dict[home_team][0]

        referee = st.selectbox('Referee', options=list(referee_map.keys()))

    with cols_away_team:
        away_team_default_index = list(team_map.keys()).index("Chelsea")
        away_team = st.selectbox('Away Team', options=list(team_map.keys()), index=away_team_default_index)
        col_away_ht_score, col_possession_away = st.columns(2)
        
        with col_away_ht_score:
            ht_away_score = st.number_input('HT Away Scored', value=0)
        with col_possession_away:
            away_possession = st.slider('Away Team Possesion', 0, 100, value=100-home_possession)
        
        st.write("____")
        
        cols_away_1, cols_away_2, cols_away_3, cols_away_4 = st.columns(4)
        
        with cols_away_1:
            away_shots_on_target = st.number_input('Shots on Target (A)', value=0)
            away_shots = st.number_input('Shots (A)', value=0)
            away_touches = st.number_input('Touches (A)', value=0)
        with cols_away_2:
            away_passes = st.number_input('Passes (A)', value=0)
            away_tackles = st.number_input('Tackles (A)', value=0)
            away_clearances = st.number_input('Clearances (A)', value=0)
        with cols_away_3:
            away_corners = st.number_input('Corners (A)', value=0)
            away_offsides = st.number_input('Offsides (A)', value=0)
            away_fouls = st.number_input('Fouls (A)', value=0)
        with cols_away_4:
            away_yellow_cards = st.number_input('Yellow Cards (A)', value=0)
            away_red_cards = st.number_input('Red Cards (A)', value=0)
        
        st.write("____")
        
        col_away_points_last_5, col_away_h2h_points_last_5 = st.columns(2)
        with col_away_points_last_5:
            away_total_points_last_5 = st.number_input('Total Points from Last 5 Games (A)', value=0)
        with col_away_h2h_points_last_5:
            away_h2h_points_last_5 = st.number_input('H2H Total Points from Last 5 Games (A)', value=0)
        
        input_data = {
            'venue': venue,
            'home_team': team_map[home_team],
            'away_team': team_map[away_team],
            'ht_home_score': ht_home_score,
            'ht_away_score': ht_away_score,
            'home_possession_%': home_possession,
            'away_possession_%': away_possession,
            'home_shots_on_target': home_shots_on_target,
            'away_shots_on_target': away_shots_on_target,
            'home_shots': home_shots,
            'away_shots': away_shots,
            'home_touches': home_touches,
            'away_touches': away_touches,
            'home_passes': home_passes,
            'away_passes': away_passes,
            'home_tackles': home_tackles,
            'away_tackles': away_tackles,
            'home_clearances': home_clearances,
            'away_clearances': away_clearances,
            'home_corners': home_corners,
            'away_corners': away_corners,
            'home_offsides': home_offsides,
            'away_offsides': away_offsides,
            'home_yellow_cards': home_yellow_cards,
            'away_yellow_cards': away_yellow_cards,
            'home_red_cards': home_red_cards,
            'away_red_cards': away_red_cards,
            'home_fouls': home_fouls,
            'away_fouls': away_fouls,
            'referee': referee_map[referee],
            'is_derby': is_derby(home_team, away_team),
            'home_total_points_last_5': home_total_points_last_5,
            'away_total_points_last_5': away_total_points_last_5,
            'home_h2h_points_last_5': home_h2h_points_last_5,
            'away_h2h_points_last_5': away_h2h_points_last_5,
        }

    # Scaling input data
    input_df = preprocess_input(input_data)

    # Load model    
    model = CatBoostClassifier().load_model('best_model.cbm')

    enter()
    if st.button("Predict", use_container_width=True):
        prediction = model.predict(input_df)[0]
        if prediction == 0:
            st.success(f"{home_team} will :red[lost] against {away_team}")
        elif prediction == 1:
            st.success(f"{home_team} will :orange[draw] against {away_team}")
        elif prediction == 2:
            st.success(f"{home_team} will :green[win] against {away_team}")
