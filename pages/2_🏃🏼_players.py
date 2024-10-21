import streamlit as st


st.set_page_config(layout='wide', page_title='Players', page_icon='🏃🏼') #Arrumando o layout da página
df_data = st.session_state['data']
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox('Clube', clubes)


df_players = df_data[(df_data['Club'] == club)]

players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox('Jogador', players)


player_stats = df_data[df_data['Name'] == player].iloc[0] #Pegando a primeira aparição do jogador
st.image(player_stats['Photo'])
st.title(player_stats['Name'])
st.markdown(f'**Clube**: {player_stats["Club"]}')
st.markdown(f'**Posição**: {player_stats["Position"]}')
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Idade**: {player_stats["Age"]}')
col2.markdown(f'**Altura**: {player_stats["Height(cm.)"] / 100}')
col3.markdown(f'**Peso**: {player_stats["Weight(lbs.)"]*0.453:.2f}')
st.divider()  #Só cria uma divisão no nosso site

st.subheader(f'**Overral**: {player_stats["Overall"]}')
st.progress(int(player_stats['Overall']))  #Vai nos dar uma medida que tem que ser de 0 a 100

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}")