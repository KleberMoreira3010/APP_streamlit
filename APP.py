import streamlit as st
import pandas as pd
import altair as alt
import datetime as dt
from PIL import Image


st.set_page_config(layout="wide")

@st.cache_data

def gerar_df():
    df = pd.read_excel(io='Mensal_of.xlsx',
                       engine = 'openpyxl',
                       sheet_name='Planilha1',
                       usecols='A:Q',
                       nrows=55616)
    return df



df= gerar_df()

colunas = ['MÊS', 'PRODUTO','REGIÃO' ,'ESTADO', 'PREÇO MÉDIO REVENDA' ]
df=df [colunas]

with st.sidebar:
    st.subheader('PRODUTIVIDADE 100%')
    logo_teste = Image.open('images.png')
    st.image(logo_teste, use_column_width=True)
    st.subheader('SELECÃO DE FILTROS')
    
    fProduto = st.selectbox('Selecione o combustível', options=df['PRODUTO'].unique())

    fEstado = st.selectbox('Selecione o Estado', options=df['ESTADO'].unique())

    dadosUsuario = df.loc[
        (df['PRODUTO'] == fProduto) & 
        (df['ESTADO'] == fEstado)
    ]

#updateDatas  = dadosUsuario['MÊS'].dt.strftime('%Y/%b')
##dadosUsuario['MÊS'] = updateDatas[0:]


st.header('PREÇOS DOS COMBUSTÍVEIS NO BRASIL: 2013 - 2023')
st.markdown('**Combustível Selecionado:** ' + fProduto)
st.markdown('**Estado:** ' + fEstado)

grafCombEstado = alt.Chart(dadosUsuario).mark_line(
    point=alt.OverlayMarkDef(color='red', size=20)
).encode(
    x= 'MÊS:T',
    y='PREÇO MÉDIO REVENDA',
    strokeWidth=alt.value(3)
).properties(
    height=700,
     width = 1300
)

st.altair_chart(grafCombEstado)

