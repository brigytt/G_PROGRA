#$ pip install streamlit --upgrade
import streamlit as st
import urllib.request
st.header("CATALOGO SISMICO 1960-2021 (IGP)")
@st.experimental_memo
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

