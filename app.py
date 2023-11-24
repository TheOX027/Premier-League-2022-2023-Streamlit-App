import pandas as pd
import streamlit as st
import altair as alt
import numpy as np
import plotly.graph_objects as go
import math
import joblib
import sklearn
from PIL import Image

st.set_page_config(
    page_title="Premier League 2022/23",
    layout='wide'
)

st.title('Premier League 2022/23 Summary')
url_editor = "https://www.linkedin.com/in/marselius-agus-dhion-374106226/"
st.markdown(f'Streamlit App by [Marselius Agus Dhion]({url_editor})', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(['Summary Information', 'Player Stats', 'Club Stats', 'Predict Season 2023/24 Match Result'])

# Tab Pertama
with tab1 : 
    opening_1 = "The Premier League season 2022/2023 has concluded and has provided some unexpected events. One of the surprising moments is when Arsenal managed to give a tough competition to Manchester City in the race for the English Premier League title. Arsenal secured the top spot in the Premier League table for 29 weeks. However, Arsenal failed to maintain their consistency until the end of the season, partly due to injuries to key players and Manchester City's consistent performance when Arsenal was not performing well. In the end, Manchester City secured the first position until the last gameweek. Another surprise came from Eddie Howe's team, Newcastle United. The last time Newcastle entered the top four was in the 2003/2004 season when Alan Shearer captained the team, and they ultimately secured the fourth position. Additionally, Manchester United also secured their spot in the Champions League."
    opening_2_1 = "Apart from Manchester City, Arsenal, and Newcastle City, who secured places in the Champions League for the next season, there are four other teams that earned spots to play outside the Premier League. Liverpool and Brighton & Hove Albion claimed the fifth and sixth positions, respectively, earning spots in the Europa League. Aston Villa secured the seventh position, allowing them to play in the Conference League next season. The last team to surprisingly earn a spot in the Europa League is West Ham. West Ham earned their place in the Europa League by winning the Conference League, defeating Fiorentina with a score of 2-1."
    opening_2_2 = "In addition to the eight teams that successfully played in European competitions, two teams, Tottenham and Chelsea, did not perform well this season. Tottenham consistently held a top-four position at the beginning of the season. Meanwhile, Chelsea, despite investing heavily, had a poor performance, partly due to the large number of players, leading to a lack of a definite lineup for the team."
    opening_3 = "Every season, three teams experience relegation. This season, the relegated teams are the Premier League champions of the 2015/2016 season, Leicester City, Leeds United, and Southampton. In the 38th gameweek or the last match, four teams were at risk of relegation, with Everton being one of them. Everton avoided relegation by winning against Bournemouth with a score of 1-0, even though Leicester won their match against West Ham with a final score of 2-1. However, Leicester was ultimately relegated. In the last gameweek, Southampton also had an interesting match, drawing against Liverpool with a significant score of 4-4."
    
    justify_text = """
    <style>
    .text-justify {
        text-align: justify;
        text-justify: inter-word;
        font-size: 16px;
    }
    </style>
    """
    

    col_header_1, col_header_2, col_header_3 = st.columns([1,1,1])
    with col_header_2 :    
        st.header('Premier League 2022/23 Overview')
    # Opening (Pemenangnya siapa, kedua, ketiga, keempat)
    col1, col11, col1_1, col1_2, col1_22 = st.columns([1,1,6,3,1])
    with col1_1 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{opening_1}</div>', unsafe_allow_html=True)
    with col1_2 :
        man_city_img = Image.open('Images/man-city.jpeg')
        st.image(man_city_img, caption='Man City Players Lifting PL Trophy',  use_column_width=True)
    
    # Opening2 (Posisi ke-5,6,7, dan West Ham)
    col2_11, col2_1, col2_2, col2_22, col2_22 = st.columns([1,3,5,1,1])
    with col2_1 : 
        west_ham_img = Image.open('Images/west-ham-conf-league.jpeg')
        st.image(west_ham_img, caption='Declan Rice with Conference League Trophy', use_column_width=True)
    with col2_2 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{opening_2_1}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{opening_2_2}</div>', unsafe_allow_html=True)
       
    col3_11, col3_111, col3_1, col3_2, col3_22 = st.columns([1,1,4,2,1])
    with col3_1 : 
        st.markdown(justify_text, unsafe_allow_html=True)
        st.markdown(f'<div class="text-justify">{opening_3}</div>', unsafe_allow_html=True)
    with col3_2 :
        lei_city_img = Image.open('Images/lei-relegated.jpg')
        st.image(lei_city_img, caption='Leicester City players after getting relegated', use_column_width=True)
    
    # Center the content
    # st.markdown('<div class="center-content"></div>', unsafe_allow_html=True)
    st.write('____________')

    # Membaca file CSV
    data = pd.read_csv('Established Datasets/Position per Gameweek.csv')
    pl_standings = pd.read_csv('Established Datasets/PL 22-23 Standings.csv', index_col=0)

    st.header('Final Standings')
    # Membuat fungsi untuk memberikan warna pada baris
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

    # Legend
    legend = {
        'Label': ['Champions League', 'Europa League', 'Conference League', 'Relegation'],
        'Warna': ['#2940D3', '#DC5F00', '#1C7947', '#CF0A0A']
    }

    df_legend = pd.DataFrame(legend)

    # Tampilkan legenda
    st.subheader('Legend : ')

    legenda_html = ""
    for i in range(len(df_legend)):
        label = df_legend.loc[i, 'Label']
        color = df_legend.loc[i, 'Warna']
        legenda_html += f'<span style="color:{color}">■</span> {label} &nbsp;&nbsp;'

    st.markdown(f'<div style="white-space: nowrap;">{legenda_html}</div>', unsafe_allow_html=True)
    
    # col1, col2 = st.columns([5, 2])
    st.write('________________')
    st.header('Performance Chart')

    # ====================================================== #
    with st.container() : 
        # Membuat select box untuk memilih klub
        clubs = data['Club'].unique()
        selected_clubs = st.multiselect('Choose Club (One or More Than One Club)', clubs)

        # Memfilter data berdasarkan klub yang dipilih
        club_data = data[data['Club'].isin(selected_clubs)]

        # Membuat line chart menggunakan Altair
        chart = alt.Chart(club_data).mark_line().encode(
            x=alt.X('Gameweek:Q', scale=alt.Scale(domain=[1, 38]), axis=alt.Axis(labelAngle=0)),
            y=alt.Y('Position:Q', scale=alt.Scale(domain=[1, 20], reverse=True), title='Position'),
            color='Club:N',
            tooltip=['Gameweek', 'Position']
        ).properties(
            width=600,
            height=400,
            title='Position Changes'
        )

        # Menambahkan titik/dot pada setiap datapoint
        chart += alt.Chart(club_data).mark_circle(size=100).encode(
            x='Gameweek',
            y='Position',
            color='Club:N',
            tooltip=['Gameweek', 'Position']
        )

        # Mengatur langkah nilai pada sumbu y
        chart = chart.configure_axisY(
            tickMinStep=1
        )

        # Menampilkan line chart pada Streamlit
        st.altair_chart(chart, use_container_width=True)


             
    # ======== Dataframe list top players Start ======== #

# Tab Kedua
with tab2 :     
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
    
    st.header("Top Scorer")
    col_scorer, col_scorer_img = st.columns([2,1])

    st.markdown('<h2 class="text-right">Top Assist</h2>', unsafe_allow_html=True)
    col_assist_img, col_assist = st.columns([1,2])

    st.header("Top Clean Sheet")
    col_cleansheet, col_cleansheet_img = st.columns([2,1])

    df_top_assist = pd.read_csv('Established Datasets/Top Asissts.csv', index_col=0)
    df_top_cleansheet = pd.read_csv('Established Datasets/Top Clean Sheet.csv', index_col=0)
    df_top_scorer = pd.read_csv('Established Datasets/Top Scorers.csv', index_col=0)

    # Players Image
    golden_boot_img = Image.open('Images/golden-boot.jpg')
    golden_glove_img = Image.open('Images/golden-glove.jpg')
    pots_img = Image.open('Images/playmaker-of-the-season.jpg')

    # Polygon Plotting 
    def normalize_log(data):
        normalized_data = [math.log(x + 1) for x in data]  # Menggunakan logaritma natural dengan penambahan 1 untuk menghindari log(0)
        return normalized_data

    def plot_polygon_with_feature_values(selected_indices, feature_names, feature_values):
        n = len(selected_indices)  # Jumlah sisi poligon yang dipilih
        angles = [i * 360 / float(n) for i in range(n)]  # Menghitung sudut untuk setiap sisi dalam derajat

        # Normalisasi feature_values
        feature_values_normalized = normalize_log(feature_values)

        # Menambahkan satu elemen tambahan untuk memastikan kesimetrisan poligon
        feature_values_normalized += [feature_values_normalized[0]]
        feature_names += [feature_names[0]]
        angles += [angles[0] + 360]

        # Membuat plotly figure
        fig = go.Figure()

        # Menambahkan trace untuk poligon
        fig.add_trace(go.Scatterpolar(
            r=feature_values_normalized,
            theta=angles,
            fill='toself',
            fillcolor='rgba(0, 123, 255, 0.2)',
            line=dict(color='rgb(0, 123, 255)'),
            hovertemplate='Nilai (Normalized): %{r:.2f}<br>Nilai (Original): %{text}<extra></extra>',
            text=feature_values,
            marker=dict(
                    size=10,  # Mengatur ukuran titik datapoint
                    symbol='circle'  # Mengatur simbol titik datapoint
            )        
        ))

        # Mengatur tampilan sumbu sudut
        fig.update_layout(
            polar=dict(
                radialaxis=dict(showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, tickmode='array', tickvals=angles, ticktext=feature_names)
            ),
            title='Players Features Value',  # Judul plot
        )

        # Mengatur ukuran plot
        fig.update_layout(width=500, height=500)

        # Menampilkan plot menggunakan Streamlit
        st.plotly_chart(fig)

    with st.container(): 
        with col_scorer :
            st.dataframe(df_top_scorer, use_container_width=True)
                    
        with col_scorer_img :
            st.image(golden_boot_img, caption='Erling Braut Halaand')
            with st.expander('Player Features Stats') : 
                feature_names = ['Headed Goals', 'Goals with right foot', 'Goals with left foot', 'Penalties Scored', 'Shots accuracy (%)', 'Big chances missed']  # Nama-nama fitur
                feature_values = [7, 6, 23, 7, 49, 28]  # Nilai fitur pada setiap sisi poligon
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
                selected_indices = [feature_names.index(feature) for feature in selected_features]
                selected_values = [feature_values[i] for i in selected_indices]
                plot_polygon_with_feature_values(selected_indices, selected_features, selected_values)
                st.write('Source : Premier League')
                
        with col_assist :
            st.dataframe(df_top_assist, use_container_width=True)
        with col_assist_img : 
            st.image(pots_img, caption='Kevin de Bruyne', use_column_width=True)
            with st.expander('Player Features Stats') :
                feature_names = ['Passes', 'Passes/nper match', 'Big chances created', 'Cross accuracy (%)', 'Through balls', 'Accurate long balls']  # Nama-nama fitur
                feature_values = [1357, 42.41, 31, 29, 28, 81]  # Nilai fitur pada setiap sisi poligon
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
                selected_indices = [feature_names.index(feature) for feature in selected_features]
                selected_values = [feature_values[i] for i in selected_indices]
                plot_polygon_with_feature_values(selected_indices, selected_features, selected_values)
                st.write('Source : Premier League')

        with col_cleansheet :
            st.dataframe(df_top_cleansheet, use_container_width=True)
        with col_cleansheet_img:
            st.image(golden_glove_img, caption='David de Gea')
            with st.expander('Player Features Stats') :
                feature_names = ['Saves', 'Penalties Saved', 'Goal Conceded', 'Erros leading to goal', 'Own goals', 'Accurate long balls', 'Punches', 'High Claims', 'Catches']  # Nama-nama fitur
                feature_values = [101, 1, 43, 2, 0, 187, 12, 14, 5]  # Nilai fitur pada setiap sisi poligon
                selected_features = st.multiselect('Select Features', feature_names, default=feature_names)
                selected_indices = [feature_names.index(feature) for feature in selected_features]
                selected_values = [feature_values[i] for i in selected_indices]
                plot_polygon_with_feature_values(selected_indices, selected_features, selected_values)
                st.write('Source : Premier League')
    
    source_data2 = "https://www.premierleague.com/stats/top/players/goals?se=489"
    st.markdown(f'Source : [Players Stats]({source_data2})', unsafe_allow_html=True)

    # ======== Dataframe list top players End ======== #

    # Fungsi untuk membuat plot poligon atribut klub dengan nilai-nilai fitur yang diberikan
    def plot_club_polygon_with_feature_values(clubs_data, feature_names):
        n = len(clubs_data)  # Jumlah klub yang dipilih
        n_features = len(clubs_data[0]['values'])  # Jumlah fitur

        # Normalisasi nilai fitur untuk setiap klub
        for club_data in clubs_data:
            club_data['values_normalized'] = normalize_log(club_data['values'])

        # Menambahkan satu elemen tambahan untuk memastikan kesimetrisan poligon
        for club_data in clubs_data:
            club_data['values_normalized'].append(club_data['values_normalized'][0])
            club_data['values'].append(club_data['values'][0])

        # Mengatur sudut untuk setiap sisi poligon
        angles = [i * 360 / float(n_features) for i in range(n_features)]
        angles += [angles[0]]  # Menghapus 360 dari daftar sudut

        # Daftar warna yang akan digunakan untuk setiap klub
        colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'pink']

        # Membuat plotly figure
        fig = go.Figure()

        # Menambahkan trace untuk setiap klub
        for i, club_data in enumerate(clubs_data):
            fig.add_trace(go.Scatterpolar(
                r=club_data['values_normalized'],
                theta=angles,
                fill='toself',
                name=club_data['name'],
                line_color=colors[i % len(colors)],  # Mengatur warna plot berdasarkan indeks klub
                hovertemplate='Club:' + club_data['name'] + '<br>Nilai (Normalized): %{r:.2f}<br>Nilai (Original): %{text}<extra></extra>',
                text=club_data['values'],
                customdata=[club_data['name']] + angles[:-1],  # Menambahkan nama klub ke data kustom
                marker=dict(
                    size=11,  # Mengatur ukuran titik datapoint
                    symbol='circle'  # Mengatur simbol titik datapoint
            )
            ))

        # Mengatur tampilan sumbu sudut
        fig.update_layout(
            polar=dict(
                radialaxis=dict(showticklabels=False, ticks=''),
                angularaxis=dict(showticklabels=True, tickmode='array', tickvals=angles[:-1], ticktext=feature_names)
            ),
            title='Club Attributes Polygon Plot',  # Judul plot
        )

        # Mengatur ukuran plot
        fig.update_layout(width=700, height=500)

        # Menampilkan plot menggunakan Streamlit
        st.plotly_chart(fig)

 
with tab3 : 
    st.header('Club Attribute Stats')      
   # Membaca data dari file CSV
    df_attack = pd.read_csv('Established Datasets/attack.csv')
    df_defence = pd.read_csv('Established Datasets/defence.csv')
    df_team_play = pd.read_csv('Established Datasets/team_play.csv')

    att_col, def_col = st.columns(2)
    col2_1, teamplay_col, col2_3 = st.columns([1,2,1])
    # Menggunakan Streamlit untuk memilih klub-klub yang ingin dibandingkan pada file attack.csv
    with att_col : 
        st.subheader('Attack Attributes')
        with st.expander('Choose Club Here'):
            club_options_attack = df_attack['Club'].unique().tolist()
            selected_clubs_attack = st.multiselect('Available Clubs', club_options_attack)
            clubs_data_attack = []

            # Mengambil data klub yang dipilih pada file attack.csv
            for club in selected_clubs_attack:
                club_data_attack = {
                    'name': club,
                    'values': df_attack[df_attack['Club'] == club].values.flatten()[2:].astype(float).tolist()
                }
                clubs_data_attack.append(club_data_attack)

            # Menampilkan poligon untuk klub-klub yang dipilih pada file attack.csv
            if len(clubs_data_attack) > 0:
                plot_club_polygon_with_feature_values(clubs_data_attack, df_attack.columns[2:].tolist())

    with def_col :
        # Menggunakan Streamlit untuk memilih klub-klub yang ingin dibandingkan pada file defence.csv
        st.subheader('Defence Attributes')
        with st.expander('Choose Club Here'):
            club_options_defence = df_defence['Club'].unique().tolist()
            selected_clubs_defence = st.multiselect('Available Clubs', club_options_defence)
            clubs_data_defence = []

            # Mengambil data klub yang dipilih pada file defence.csv
            for club in selected_clubs_defence:
                club_data_defence = {
                    'name': club,
                    'values': df_defence[df_defence['Club'] == club].values.flatten()[2:].astype(float).tolist()
                }
                clubs_data_defence.append(club_data_defence)

            # Menampilkan poligon untuk klub-klub yang dipilih pada file defence.csv
            if len(clubs_data_defence) > 0:
                plot_club_polygon_with_feature_values(clubs_data_defence, df_defence.columns[2:].tolist())

    with teamplay_col : 
        # Menggunakan Streamlit untuk memilih klub-klub yang ingin dibandingkan pada file team_play.csv
        st.subheader('Team Play Attributes')
        with st.expander('Choose Club Here'):
            club_options_team_play = df_team_play['Club'].unique().tolist()
            selected_clubs_team_play = st.multiselect('Available Clubs', club_options_team_play)
            clubs_data_team_play = []

            # Mengambil data klub yang dipilih pada file team_play.csv
            for club in selected_clubs_team_play:
                club_data_team_play = {
                    'name': club,
                    'values': df_team_play[df_team_play['Club'] == club].values.flatten()[2:].astype(float).tolist()
                }
                clubs_data_team_play.append(club_data_team_play)

            # Menampilkan poligon untuk klub-klub yang dipilih pada file team_play.csv
            if len(clubs_data_team_play) > 0:
                plot_club_polygon_with_feature_values(clubs_data_team_play, df_team_play.columns[2:].tolist())
    
    source_data3 = "https://www.premierleague.com/stats/top/clubs/wins?se=489"
    st.markdown(f'Source : [Premier League Club Stats]({source_data3})', unsafe_allow_html=True)

    
with tab4 :         
    model_path = "model.joblib"
    model = open(model_path, "rb")
    # model = joblib.load("model.joblib")
    
    st.header('Predict Premier League 2023/24 Match Result')
    
    # Menampilkan expander di sidebar
    with st.expander("Features Information (Click Here)"):
        col_info, col_club2 = st.columns([3,1])
        with col_info : 
            st.write(f"- Recent Form Home & Away : Sum of scores in the last 5 matches")                    
            st.write(f"- Unbeaten Streak Home & Away : Total current unbeaten streak")
            st.write(f"- Win Streak Home & Away : Total current winning streak")
            st.write(f"- Performance Change Home & Away : Difference in current score and the 5-match rolling mean for the home team")
            st.image('Images/performance_change.png')
            st.write(f"- Total Home & Away Points Prev. 5 Matches : Total Points Gained Last 5 Matches")
            st.write(f"- Possession Growth** : Diffrence in possession percentage between the away and home teams, negative indicating the home team has higher possession")
            st.write(f"- Avg. Goals at Venue : Average number of goals scored by the home team at a their own stadium")

        st.write('')
        st.write(f'\nInformation => ** : Automated Filled')
                                    
    cols_home, cols_penengah, cols_away = st.columns([4,1,4])
    team_map = {
        "Arsenal" : 0, "Aston Villa" : 1, "Bournemouth" : 6, 
        "Brentford" : 7, "Brighton & Hove Albion" : 8,
        "Burnley" : 9, "Chelsea" : 12, "Crystal Palace" : 13, 
        "Everton" : 15, "Fulham" : 16, "Liverpool" : 21,
        "Luton Town" : 100, "Man. City" : 22, "Man. United" : 23, 
        "Newcastle United" : 26, "Nott'm Forrst" : 28,
        "Sheffield United" : 32, "Tottenham Hostpur" : 37, 
        "West Ham United" : 40, "Wolves" : 42
        }
    no_team_options = [0, 1, 6, 7, 8, 
                       9, 12, 13, 15, 16, 21, 
                       100, 22, 23, 26, 28, 
                       32, 37, 40, 42]

    with cols_home:
        home_team = st.selectbox('Home Team', options=list(team_map.keys()))
        home_possesion = st.slider('Home Team Possesion',0, 100, value=0)
        st.write("____")

        cols_home_1, cols_home_2, cols_home_3, cols_home_4, cols_home_5 = st.columns(5)
        with cols_home_1 : 
            ht_home_score = st.text_input('HT Home Scored', value=1)
            home_touches = st.text_input('Home Touches', value=1)
        with cols_home_2 :
            home_shots_on_target = st.text_input('Home Shots on Target', value=1)
            home_passes = st.text_input('Home Passes', value=1)
        with cols_home_3 :
            home_shots = st.text_input('Home Shots', value=1)
            home_tackles = st.text_input('Home Tackles', value=1)
        with cols_home_4 :
            home_clearances = st.text_input('Home Clearances', value=1)
            home_red_cards = st.text_input('Home Red Card', value=1)
        with cols_home_5 :
            home_offsides = st.text_input('Home Offsides', value=1)
            home_yellow_cards = st.text_input('Home Yellow Card', value=1)
        
        st.write("____")
        cols_home_1_1, cols_home_2_2 = st.columns(2)
        st.write("____")

        with cols_home_1_1 :
            recent_form_home = st.slider('Recent Form Home (Total Goals Scored)', 0, 30, value=1)
            win_streak_home = st.slider('Win Streak Home (Days)', 0, 365, value=1)
        with cols_home_2_2 :
            unbeaten_streak_home = st.slider('Unbeaten Streak Home (Days)', 0, 365, value=1)
            performance_change_home = st.slider('Performance Change Home', -10.0, 10.0, value=1.0)
            total_points_prev_matches_home = st.slider('Total Home Points Prev. 5 Matches', 0, 15)

    
    with cols_away:
        away_team = st.selectbox('Away Team', options=list(team_map.keys()))
        away_possesion = st.slider('Away Team Possesion',0, 100, value=100-home_possesion)
        st.write("____")

        cols_away_1, cols_away_2, cols_away_3, cols_away_4, cols_away_5 = st.columns(5)
        with cols_away_1 : 
            ht_away_score = st.text_input('HT Away Scored', value=1)
            away_touches = st.text_input('Away Touches', value=1)
        with cols_away_2 :
            away_shots_on_target = st.text_input('Away Shots on Target', value=1)
            away_passes = st.text_input('Away Passes', value=1)
        with cols_away_3 :
            away_shots = st.text_input('Away Shots', value=1)
            away_tackles = st.text_input('Away Tackles', value=1)
        with cols_away_4 :
            away_clearances = st.text_input('Away Clearances', value=1)
            away_red_cards = st.text_input('Away Red Card', value=1)
        with cols_away_5 :
            away_offsides = st.text_input('Away Offsides', value=1)
            away_yellow_cards = st.text_input('Away Yellow Card', value=1)
                     
        st.write("____")
        cols_away_1_1, cols_away_2_2 = st.columns(2)
        st.write("____")        
        with cols_away_1_1 :
            recent_form_away = st.slider('Recent Form Away (Total Goals Scored)', 0, 30, value=1)
            win_streak_away = st.slider('Win Streak Away (Days)', 0, 365, value=1)
            total_points_prev_matches_away = st.slider('Total Away Points Prev. 5 Matches', 0, 15)

        with cols_away_2_2 :
            unbeaten_streak_away = st.slider('Unbeaten Streak Away (Days)', 0, 365, value=1)
            performance_change_away = st.slider('Performance Change Away', -10.0, 10.0, value=1.0)
    
    col_1, cols_other_1, cols_other_1_1, cols_other_1_1_1, cols_other_2, cols_other_2_2, cols_other_2_2_2, cols_other_3, col_3 = st.columns([1, 6, 1, 1, 3, 1, 1, 6, 1])
    referee_map = {
        'Michael Oliver' : 31, 'Andy Madley' : 25,
        'Robert Jones' : 11, 'Peter Bankes' : 40,
        'Craig Pawson' : 41, 'Jarred Gillett' : 23,
        'Darren England' : 21, 'Michael Salisbury' : 39,
        'John Brooks' : 42, 'Tony Harrington' : 44,
        'David Coote' : 47, 'Graham Scott' : 27,
        'Thomas Bramall' : 17, 'Chris Kavanagh' : 35
    }
    with cols_other_1 : 
        possession_growth = st.slider('Possession Growth**', -100, 100, value=away_possesion-home_possesion)
    with cols_other_2 : 
        referee = st.selectbox('Referee', options=list(referee_map.keys()))
    with cols_other_3 :  
        avg_goals_at_venue = st.slider('Avg. Goals at Home Team Stadium', 0, 5, value=0)
    
    home_goal_to_shot_ratio = float(home_shots_on_target) / float(home_shots)
    away_goal_to_shot_ratio = float(away_shots_on_target) / float(away_shots)
    
    successful_passes_home = int(home_passes) - int(home_clearances)
    successful_passes_away = int(away_passes) - int(away_clearances)
    
    home_disciplinary_points = int(home_yellow_cards)*1 + int(home_red_cards)*3 
    away_disciplinary_points = int(away_yellow_cards)*1 + int(away_red_cards)*3 
    
    home_touches_ratio = float(home_touches) / (float(home_touches) + float(away_touches))
    away_touches_ratio = float(away_touches) / (float(home_touches) + float(away_touches))
    
    home_clearances_ratio = float(home_clearances) / (float(home_clearances) + float(away_clearances))
    away_clearances_ratio = float(away_clearances) / (float(home_clearances) + float(away_clearances))
    
    home_tackles_ratio = float(home_tackles) / (float(home_tackles) + float(away_tackles))
    away_tackles_ratio = float(away_tackles) / (float(home_tackles) + float(away_tackles))
    
    home_offsides_ratio = float(home_offsides) / (float(home_offsides) + float(away_offsides))
    away_offsides_ratio = float(away_offsides) / (float(home_offsides) + float(away_offsides))

    
    if st.button('PREDICT', use_container_width=True) : 
        home_team = team_map.get(home_team)
        away_team = team_map.get(away_team)
        referee = referee_map.get(referee)
        
        ht_home_score = (int(ht_home_score) - 0) / (5-0)
        ht_away_score = (int(ht_away_score) - 0) / (5-0)
        
        home_shots_on_target = (int(home_shots_on_target) - 0) / (17-0)
        away_shots_on_target = (int(away_shots_on_target) - 0) / (15-0)
        
        home_shots = (int(home_shots) - 0) / (44-0)
        away_shots = (int(away_shots) - 0) / (33-0)
        
        home_passes = (int(home_passes) - 155) / (1015 - 155)
        away_passes = (int(away_passes) - 148) / (976 - 148)
        
        home_clearances = (int(home_clearances) - 0) / (107 - 0)
        away_clearances = (int(away_clearances) - 1) / (129 - 1)
        
        home_yellow_cards = (int(home_yellow_cards) - 0) / (7-0)
        away_yellow_cards = (int(away_yellow_cards) - 0) / (9-0)
        
        home_red_cards = (int(home_red_cards) - 0) / (2-0)
        away_red_cards = (int(away_red_cards) - 0) / (2-0)
        
        home_touches = (int(home_touches) - 335) / (1160-335)
        away_touches = (int(away_touches) - 294) / (1116-294)
        
        home_clearances = (int(home_clearances) - 0) / (107-0)
        away_clearances = (int(away_clearances) - 1) / (129-1)
        
        home_tackles = (int(home_tackles)-3) / (48-3)
        away_tackles = (int(away_tackles)-3) / (50-3)
        
        home_offsides = (int(home_offsides)-0) / (14-0)
        away_offsides = (int(away_offsides)-0) / (12-0)
        
        
        input_data = np.array([[
                ht_home_score, ht_away_score,
                home_shots_on_target, away_shots_on_target,
                home_shots, away_shots,
                home_goal_to_shot_ratio, away_goal_to_shot_ratio,
                successful_passes_home, successful_passes_away,
                performance_change_home, performance_change_away,
                recent_form_home, recent_form_away,
                win_streak_home, win_streak_away,
                avg_goals_at_venue, home_disciplinary_points,
                unbeaten_streak_home, unbeaten_streak_away,
                total_points_prev_matches_home, total_points_prev_matches_away,
                possession_growth,
                home_touches_ratio, away_touches_ratio,
                home_clearances_ratio, away_clearances_ratio,
                home_team, away_team,
                referee, away_disciplinary_points,
                home_tackles_ratio, away_tackles_ratio,
                home_offsides_ratio, away_offsides_ratio
            ]])
        
        result_prediction = model.predict(input_data)
        
        # 'result': {'W': 0, 'D': 1, 'L': 2},
        if result_prediction[0] == 0:
            st.success(f'Home Team Will Win')
        elif result_prediction[0] == 1:
            st.success('Home Team Will Draw')
        elif result_prediction[0] == 2:
            st.success('Home Team Will Lost')