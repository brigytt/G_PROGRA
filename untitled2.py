#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image

#@st.experimental_memo

with st.sidebar:
   st.sidebar.header('Programación avanzada')
   image = Image.open('Logo_Oficial (1).png')
   st.image(image,use_column_width=True)
   selected = option_menu(
      menu_title = 'Menú',
      options = ['Inicio','Informe','Equipo'],
      icons = ['house','book','people'],
      menu_icon = 'cast',
      default_index = 0,
   )
if selected == 'Inicio':
   st.markdown("<h1 style ='text-align: center'> CATALOGO SISMICO 1960-2021 (IGP) </h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.write('La base de datos sobre la actividad sísmica en el país fue realizada por el Instituto Geofísico del Perú (IGP) desde el año de 1960 hasta el 2021. El IGP es la institución responsable del monitoreo de la actividad sísmica del país, y contiene todos aquellos sismos percibidos por la población y registrados por la Red Sísmica Nacional desde 1960, fecha en la que se inicia la vigilancia instrumental de la sismicidad en el Perú.')
   st.write('¿Por qué es importante saber sobre los datos de los sismos?')
   col1, col2 =st.columns(2)
   image = Image.open('imagen 1.jpg')
   col1.write("Los desastres naturales han acompañado el desarrollo de la humanidad a lo largo de la historia; por ello, rescatar y analizar a los sismos desde la historia ayuda a comprender no sólo las acciones humanas en torno a ellos, sino también a descifrar las características y patrones de comportamiento de la actividad sísmica, lo que puede ayudar a los sismólogos, geólogos y otros especialistas a elaborar con mayores datos y precisión, los mapas de riesgo. Además, tener conocimiento sobre estos fenómenos nos permitirá construir una sociedad preventiva, la vulnerabilidad física y la vulnerabilidad social nos ayudará a contar con herramientas –como simulacros y mochilas de emergencia– para estar preparados ante lo que podemos esperar en un evento real.")          
   col2.image(image,use_column_width=True)       
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
if selected == 'Informe':
   st.markdown("<h1 style ='text-align: center'> CATÁLOGO SÍSMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   def download_data():
      url="https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv"
      df=pd.read_csv('Catalogo1960_2021.xlsx')
      return df
   year_select=st.sidebar.selectbox('Fecha', list(reversed(range(1960,2021))))
   def load_data(year):
      df=download_data()
      df=df.astype({'FECHA_UTC':'str'})
      df['HORA_UTC'] = pd.to_numeric(df['HORA_UTC'])
      df['MAGNITUD']= pd.to_numeric(df['MAGNITUD'])
      grouped=df.groupby(df.FECHA_UTC)
      df_year=grouped.get_group(year)
      return df_year
   
   data_FECHA=load_data(str(year_select))
   sorted_DEPARTAMENTO = sorted(data_FECHA.DEPARTAMENTO.unique())
   selected_departamento=st.sidebar.multiselect('Departamento',sorted_DEPARTAMENTO, sorted_DEPARTAMENTO)
   
   unique_data=['HORA_UTC','MAGNITUD']
   selected_data= st.sidebar.multiselect('Clasificación', unique_data,unique_data)
   df_selected=data_FECHA[(data_FECHA.DEPARTAMENTO.isin(selected_departamento))]
   
   def remove_columns(dataset, cols):
      return dataset.drop(cols, axis=1)
   cols=np.setdiff1d(unique_data, selected_data)
   st.subheader('Mostrar data de distrito(s) y clasificacion(s) seleccionado(s)')
   data=remove_columns(df_selected, cols)
   st.write('Dimensiones: ' + str(data.shape[0]) + ' filas y ' + str(data.shape[1]) + ' columnas')
   st.dataframe(data)
   #-----------------------------------------------------------------------------------------------
   st.write("------------------------------------------------------------------------------------------------------------------------------------")
   set_departamentos = np.sort(c['DEPARTAMENTO'].dropna().unique())
   #Seleccion del departamento
   opcion_departamento = st.selectbox('Selecciona un departamento', set_departamentos)
   df_departamentos = c[c['DEPARTAMENTO'] == opcion_departamento]
   num_filas = len(df_departamentos.axes[0]) 

   #Construccion del set/list de provincias (Valores unicos sin NA)
   set_provincias = np.sort(df_departamentos['PROVINCIA'].dropna().unique())
   #Seleccion de la provincia
   opcion_provincia = st.selectbox('Selecciona una provincia', set_provincias)
   df_provincias = df_departamentos[df_departamentos['PROVINCIA'] == opcion_provincia]
   num_filas = len(df_provincias.axes[0]) 
   set_distritos = np.sort(df_departamentos['DISTRITO'].dropna().unique())
   #Seleccion de la distrito
   opcion_distrito = st.selectbox('Selecciona un distrito', set_distritos)
   df_distritos = df_departamentos[df_departamentos['DISTRITO'] == opcion_distrito]
   num_filas = len(df_distritos.axes[0])
   
if selected == 'Equipo':
   st.markdown("<h1 style ='text-align: center'> ¿Quiénes somos?:</h1>", unsafe_allow_html= True)
   st.markdown("---")
   st.write('Somos un grupo de estudiantes del V ciclo de la carrera de Ingeniería Ambiental de la Universidad Peruano Cayetano Heredia (UPCH). Mediante el procesamiento y visualización de datos se brindará todos los parámetros que caracterizan un sismo con el objetivo de constituirse como una base útil para la realización de estudios en sismología.')
   col1, col2, col3= st.columns(3)
   image1 = Image.open('f238361e-ccb8-48d1-8993-1de25db1c866.jpg')
   col1.header("Miguel Calistro Aguilar")
   col1.image(image1, use_column_width=True)
   image2 = Image.open('WhatsApp Image 2022-11-27 at 23.17.23.jpeg')
   col2.header("Brigytt Contreras Melgar")
   col2.image(image2, use_column_width=True)
   image3 = Image.open('WhatsApp Image 2022-11-28 at 19.18.22.jpeg')
   col3.header("Daniel Chamorro Grados")
   col3.image(image3, use_column_width=True)
