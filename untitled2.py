#$ pip install streamlit --upgrade
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import urllib.request
import base64
st.header("CATALOGO SISMICO 1960-2021 (IGP)")
st.markdown("""Este dataset muestra los datos """)
@st.experimental_memo
def download_data():
   url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.xlsx"
   filename="Catalogo1960_2021.xlsx"
   urllib.request.urlretrieve(url,filename)
   df=pd.read_csv('Catalogo1960_2021.xlsx')
   return df
c=download_data()
st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
st.dataframe(c)
st.subheader("Características del Dataset")
st.write(c.describe())
