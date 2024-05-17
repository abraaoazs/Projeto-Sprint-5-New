import pandas as pd
import plotly.express as px
import streamlit as st



st.header("Gráfico e Histograma de vendas de carros nos EUA")

car_data = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    fig = px.histogram(car_data, x = 'odometer')

    st.plotly_chart(fig, use_container_width= True)




hist_button_2 = st.button('Criar gráfico de dispersão')

if hist_button_2:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de preço por milhas percorridas')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width= True)
