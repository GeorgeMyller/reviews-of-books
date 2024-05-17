#app2.py
#App Web Asimov Academy
#usar streamlist (https://streamlit.io/)
#pandas manipulação e tratamento de dados
#plotly graficos com informações do pandas

#pandas carrega os dados e manipula o tremlist carrega e manda os dados e plotlist cria os graficos
# Install necessary packages
#pip3 install streamlit 
#pip install pandas
#pip install plotly

#importando  as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

#configuração da página no streamlit
st.set_page_config(layout="wide")
#definindo variaveis e carregando dados em csv com pandas
df_reviws = pd.read_csv('datasets/customerreviews.csv')
df_top_100_books = pd.read_csv('datasets/Top_100_Trending_Books.csv')

books = df_top_100_books['book title'].unique()
book = st.sidebar.selectbox('Books', books)

df_book = df_top_100_books[df_top_100_books['book title'] == book]
df_reviews_f = df_reviws[df_reviws['book name'] == book]

book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = f"${df_book['book price'].iloc[0]}"
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)

col1, col2, col3 = st.columns(3)
col1.metric("Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year Released", book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])