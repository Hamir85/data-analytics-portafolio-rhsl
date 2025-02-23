import streamlit as st
import pandas as pd
import sidetable as stb
import plotly.express as px 

data_cars= pd.read_csv('datasets/vehicles_us.csv')

st.header('Data Analytics Portafolio Renato Septien')
st.write('Analisis esxloratorio de los datos de Vehiculos')


st.write('Revision de primeras filas de los datos')
st.dataframe(data_cars.head())

histo_botton= st.button('Construir histograma de los precios de los vehiculos')

if histo_botton:
    st.write('Creacion del histograma para la distribiucion de los precios de los carros')

    fig = px.histogram(data_cars, x= 'price')

    st.plotly_chart(fig)

histo_botton_type = st.button('Costruir un histograma del tipo de vehiculos')

if histo_botton_type:
    st.write('Creacion de histograma por tipo de vehiculo')

    fig_2 = px.histogram(data_cars, x = 'type')

    st.plotly_chart(fig_2)
