#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu

#st.header("CATALOGO SISMICO 1960-2021 (IGP)")
#@st.experimental_memo

with st.sidebar:
   st.markdown("CATALOGO SISMICO 1960-2021 (IGP)")
   st.sidebar.header('Programación avanzada')
   selected = option_menu(
      menu_title = 'Menú',
      options = ['Inicio','Informe','Equipo'],
      icons = ['house','book','people'],
      menu_icon = 'cast',
      default_index = 0,
   )
if selected == 'Inicio':
   st.markdown("<h1 style ='text-align: center'> CATALOGO SISMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.header("Dataset")
   
   def download_data():
      url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      filename="Catalogo1960_2021.xlsx"
      urllib.request.urlretrieve(url,filename)
      df=pd.read_csv('Catalogo1960_2021.xlsx')
      return df
   c=download_data()
   st.write('Dimensiones: ' + str(c.shape[0]) + ' filas y ' + str(c.shape[1]) + ' columnas')
   st.dataframe(c)
   st.subheader("Características del Dataset")
   st.write(c.describe())

#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/brigytt/G_PROGRA/main/Catalogo1960_2021.csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')



