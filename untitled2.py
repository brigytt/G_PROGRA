#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

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
   st.markdown("<h1 style ='text-align: center'> CATÁLOGO SÍSMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.header("Los desastres naturales han acompañado el desarrollo de la humanidad a lo largo de la historia; por ello, rescatar y analizar a los sismos desde la historia ayuda a comprender no sólo las acciones humanas en torno a ellos, sino también a descifrar las características y patrones de comportamiento de la actividad sísmica, lo que puede ayudar a los sismólogos, geólogos y otros especialistas a elaborar con mayores datos y precisión, los mapas de riesgo.")
   st.header(" Además, tener conocimiento sobre estos fenómenos nos permitirá construir una sociedad preventiva, la vulnerabilidad física y la vulnerabilidad social nos ayudará a contar con herramientas –como simulacros y mochilas de emergencia– para estar preparados ante lo que podemos esperar en un evento real.")          
           

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
   
image = Image.open('imagen 1.jpg')
st.image(image, caption='La contaminación por el parque automotor antiguo es un problema en Lima Metropolitana', use_column_width=True)

#url del archivo en formato raw
url = 'https://raw.githubusercontent.com/brigytt/G_PROGRA/main/Catalogo1960_2021.csv'
datos = pd.read_csv(url,sep= ',')
st.line_chart(data=datos, x='FECHA_UTC', y='MAGNITUD')



