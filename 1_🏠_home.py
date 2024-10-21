#Projeto FIFA usando Streamlit

import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if 'data' not in st.session_state:
    df_data = pd.read_csv(r'C:\Users\jrodr\Downloads\Asimov\Python Office\Criando Aplicativos Web com Streamlit\Projeto Fifa\datasets\CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown("# FIFA 2023 OFFICIAL DATASET!⚽️")
st.sidebar.markdown("Desenvolvido por Rodrigo Moraes")

btn = st.button('Acesse os dados do Kaggle')  #Colocar um botão no código. Ele começa por default como False, quando alguém clica, fica True
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 

    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)

#Ainda não fizemos o carregamento dos dados e a disposição dele no nosso state. Ou seja, quero que uma pessoa abra o home
#carregue o nosso state e já distribua essa informação para as outras páginas

#Usando a técnica que aprendemos no módulo de cacheamento. Foi adicionado la em cima com a lógica if 'data' not in st.session_state