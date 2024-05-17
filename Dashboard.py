#app2.py
#App Web Asimov Academy
#usar streamlist (https://streamlit.io/)
#pandas manipulação e tratamento de dados
#plotly graficos com informações do pandas

#pandas carrega os dados e manipula o tremlist carrega e manda os dados e plotlist cria os graficos
# Install necessary packages
"""
! pip3 install -q -U streamlit 
! pip3 install -q -U pandas
! pip3 install -q -U plotly
"""
#importando  as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

#configuração da página no streamlit
st.set_page_config(layout="wide")
#definindo variaveis e carregando dados em csv com pandas
df_reviws = pd.read_csv('datasets/customerreviews.csv')
df_top_100_books = pd.read_csv('datasets/Top_100_Trending_Books.csv')

price_max = df_top_100_books['book price'].max()
price_min = df_top_100_books['book price'].min()

max_price = st.sidebar.slider('Faixa de preço', price_min, price_max)
df_books = df_top_100_books[df_top_100_books['book price'] <= max_price]
df_books

col1, col2 = st.columns(2)
#st.write("Quantidade de livros por ano de publicação: ")
#st.bar_chart(df_books['year of publication'].value_counts().sort_index())
fig = px.histogram(df_books['book price']) 
col1.plotly_chart(fig)
fig2 =px.bar(df_books['year of publication'].value_counts())
col2.plotly_chart(fig2)

#criar nova pagina 


exit()



