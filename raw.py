import streamlit as st
import pandas as pd
import numpy as np

DATE_TIME = 'date/time'

@st.cache
def load_data(nrows):
    data=pd.read_csv("uber-raw-data-sep14.csv", nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase,axis='columns', inplace=True)
    data[DATE_TIME] = pd.to_datetime(data[DATE_TIME])
    return data

data = load_data(10000)

hour = st.slider('Selected hour',0,0,23,1)
data = data[data[DATE_TIME].dt.hour == hour]

if st.checkbox('View Data'):
    st.subheader('Raw Data')
    st.write(data)


st.subheader('Data by Minute at %sh' % hour)    
st.bar_chart(np.histogram(data[DATE_TIME].dt.minute, bins=60, range=(0,60))[0])

st.subheader('Geodata at %sh' % hour)
st.map(data)
