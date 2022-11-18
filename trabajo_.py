import streamlit as st
import pandas as pd
import numpy as np
import os 
st.title('CATALOGO SISMICO 1960-2021 (IGP) ')
mainpath = "drive/MyDrive/Trabajo"
filename = "Catalogo1960_2021.xlsx"
fullpath = os.path.join(mainpath,filename)
df = pd.read_excel(fullpath)
df.head(2000)
