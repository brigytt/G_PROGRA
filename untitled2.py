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
   st.info('La base de datos sobre la actividad sísmica en el país fue realizada por el Instituto Geofísico del Perú (IGP) desde el año de 1960 hasta el 2021. El IGP es la institución responsable del monitoreo de la actividad sísmica del país, y contiene todos aquellos sismos percibidos por la población y registrados por la Red Sísmica Nacional desde 1960, fecha en la que se inicia la vigilancia instrumental de la sismicidad en el Perú.')
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
   
if selected == 'Informe':
   st.markdown("<h1 style ='text-align: center'> CATÁLOGO SÍSMICO 1960-2021 (IGP):</h1>", unsafe_allow_html= True)
   st.markdown("---")
   #DATOS POR FECHA
   
   #DATOS POR DEPARTAMENTO

   opcion_dataset = st.selectbox('Eliga el Departamento',('SELECCIONAR','AMAZONAS','ANCASH','APURIMAC','AREQUIPA','AYACUCHO','UCAYALI','TUMBES','TACNA','CAJAMARCA','CALLAO','SAN MARTIN','PUNO','CUZCO','PIURA','PASCO','HUANCAVELICA','HUANUCO','ICA','JUNIN','LA LIBERTAD','LAMBAYEQUE','LIMA','LORETO','MADRE DE DIOS','MAR'))
   estado = '-'
   if opcion_dataset == 'SELECCIONAR':
      df_visualizacion = None
   datos_Amazonas= pd.read_csv('Amazonas.csv')
   if opcion_dataset == 'AMAZONAS':
      df_visualizacion = datos_Amazonas
      st.dataframe(df_visualizacion)
   datos_Ancash= pd.read_csv('Ancash.csv')
   if opcion_dataset == 'ANCASH':
      df_visualizacion = datos_Ancash
      st.dataframe(df_visualizacion)
   datos_Apurimac= pd.read_csv('Apurimac.csv')
   if opcion_dataset == 'APURIMAC':
      df_visualizacion = datos_Apurimac
      st.dataframe(df_visualizacion)
   datos_Arequipa= pd.read_csv('Arequipa.csv')
   if opcion_dataset == 'AREQUIPA':
      df_visualizacion = datos_Arequipa
      st.dataframe(df_visualizacion)
   datos_Ayacucho= pd.read_csv('Ayacucho.csv')
   if opcion_dataset == 'AYACUCHO':
      df_visualizacion = datos_Ayacucho
      st.dataframe(df_visualizacion)
   datos_Cajamarca= pd.read_csv('Cajamarca.csv')
   if opcion_dataset == 'CAJAMARCA':
      df_visualizacion = datos_Cajamarca
      st.dataframe(df_visualizacion)
   datos_Callao= pd.read_csv('Callao.csv')
   if opcion_dataset == 'CALLAO':
      df_visualizacion = datos_Callao
      st.dataframe(df_visualizacion)
   datos_Cuzco= pd.read_csv('Cuzco.csv')
   if opcion_dataset == 'CUZCO':
      df_visualizacion = datos_Cuzco
      st.dataframe(df_visualizacion)
   datos_Huancavelica= pd.read_csv('Huancavelica.csv')
   if opcion_dataset == 'HUANCAVELICA':
      df_visualizacion = datos_Huancavelica
      st.dataframe(df_visualizacion)
   datos_Huanuco= pd.read_csv('Huanuco.csv')
   if opcion_dataset == 'HUANUCO':
      df_visualizacion = datos_Huanuco
      st.dataframe(df_visualizacion)
   datos_Ica= pd.read_csv('Ica.csv')
   if opcion_dataset == 'ICA':
      df_visualizacion = datos_Ica
      st.dataframe(df_visualizacion)
   datos_Junin= pd.read_csv('Junin.csv')
   if opcion_dataset == 'JUNIN':
      df_visualizacion = datos_Junin
      st.dataframe(df_visualizacion)
   datos_LaLibertad= pd.read_csv('La Libertad.csv')
   if opcion_dataset == 'LA LIBERTAD':
      df_visualizacion = datos_LaLibertad
      st.dataframe(df_visualizacion)
   datos_Lambayeque= pd.read_csv('Lambayeque.csv')
   if opcion_dataset == 'LAMBAYEQUE':
      df_visualizacion = datos_Lambayeque
      st.dataframe(df_visualizacion)
   datos_Lima= pd.read_csv('Lima.csv')
   if opcion_dataset == 'LIMA':
      df_visualizacion = datos_Lima
      st.dataframe(df_visualizacion)
   datos_Loreto= pd.read_csv('Loreto.csv')
   if opcion_dataset == 'LORETO':
      df_visualizacion = datos_Loreto
      st.dataframe(df_visualizacion)
   datos_MadredeDios= pd.read_csv('Madre de Dios.csv')
   if opcion_dataset == 'MADRE DE DIOS':
      df_visualizacion = datos_MadredeDios
      st.dataframe(df_visualizacion)
   datos_Mar= pd.read_csv('Mar.csv')
   if opcion_dataset == 'MAR':
      df_visualizacion = datos_Mar
      st.dataframe(df_visualizacion)
   datos_Pasco= pd.read_csv('Pasco.csv')
   if opcion_dataset == 'PASCO':
      df_visualizacion = datos_Pasco
      st.dataframe(df_visualizacion)
   datos_Piura= pd.read_csv('Piura.csv')
   if opcion_dataset == 'PIURA':
      df_visualizacion = datos_Piura
      st.dataframe(df_visualizacion)
   datos_Puno= pd.read_csv('Puno.csv')
   if opcion_dataset == 'PUNO':
      df_visualizacion = datos_Puno
      st.dataframe(df_visualizacion)
   datos_SanMartin= pd.read_csv('San Martin.csv')
   if opcion_dataset == 'SAN MARTIN':
      df_visualizacion = datos_SanMartin
      st.dataframe(df_visualizacion)
   datos_Tacna= pd.read_csv('Tacna.csv')
   if opcion_dataset == 'TACNA':
      df_visualizacion = datos_Tacna
      st.dataframe(df_visualizacion)
   datos_Tumbes= pd.read_csv('Tumbes.csv')
   if opcion_dataset == 'TUMBES':
      df_visualizacion = datos_Tumbes
      st.dataframe(df_visualizacion)
   datos_Ucayali= pd.read_csv('Ucayali.csv')
   if opcion_dataset == 'UCAYALI':
      df_visualizacion = datos_Ucayali
      st.dataframe(df_visualizacion)
   
   #DATOS POR PAÍS
   opcion_dataset = st.selectbox('Eliga el país',('SELECCIONAR','BOLIVIA','BRASIL','CHILE','COLOMBIA','ECUADOR'))
   estado = '-'
   if opcion_dataset == 'SELECCIONAR':
      df_visualizacion = None
   datos_Bolivia= pd.read_csv('Bolivia.csv')
   if opcion_dataset == 'BOLIVIA':
      df_visualizacion = datos_Bolivia
      st.dataframe(df_visualizacion)
   datos_Brasil= pd.read_csv('Brasil.csv')
   if opcion_dataset == 'BRASIL':
      df_visualizacion = datos_Brasil
      st.dataframe(df_visualizacion)
   datos_Chile= pd.read_csv('Chile.csv')
   if opcion_dataset == 'CHILE':
      df_visualizacion = datos_Chile
      st.dataframe(df_visualizacion)
   datos_Colombia= pd.read_csv('Colombia.csv')
   if opcion_dataset == 'COLOMBIA':
      df_visualizacion = datos_Colombia
      st.dataframe(df_visualizacion)
   datos_Ecuador= pd.read_csv('Ecuador.csv')
   if opcion_dataset == 'ECUADOR':
      df_visualizacion = datos_Ecuador
      st.dataframe(df_visualizacion)

   
   
   #url archivo raw
   url= 'https://www.datosabiertos.gob.pe/sites/default/files/Catalogo1960_2021.csv'
   datos=pd.read_csv(url, sep=',')
   st.subheader('Gráfico de Epicentro vs Fecha_UTC')
   st.write('')
   st.line_chart(data=datos, x='EPICENTRO', y='FECHA_UTC')
   st.subheader('Gráfico de Magnitud vs Departamento')
   st.write('')
   st.line_chart(data=datos, x='MAGNITUD', y='DEPARTAMENTO')
   st.subheader('Gráfico de Fecha_UTC vs Departamento')
   st.write('')
   st.line_chart(data=datos, x='FECHA_UTC', y='DEPARTAMENTO')
   st.subheader('Gráfico de Profundidad vs Departamento')
   st.write('')
   st.line_chart(data=datos, x='PROFUNDIDAD', y='DEPARTAMENTO')
	

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
   
