'''Create a Streamlit dashboard using the vehicles.csv datafile that allows users to 
explore vehicle data dynamically. Filter the data by car manufacturer. 
*Imp - Understand the data and columns present in the data. 
1. User should be able to select the car manufacturer with the help of a 
select-box 
2. Filter the data based on the selected manufacturer and plot 4 types of 
graphs. 
3. The graphs should be relevant and should make sense. 
1. For ex. Plot a scatterplot of Engine size v/s fuel efficiency.'''
import streamlit as st
import pandas as pd
import numpy as np
data=pd.read_csv('cars_clus.csv')

st.title('Vehicle Data Dashboard')
st.write(data.head(5))
manufacture=data['manufact'].unique()
# st.write(manufacture)
selected_manufacturer=st.selectbox('**Select Manufacturer**',manufacture,index=None,)
st.write(f'Select data for {selected_manufacturer} manufacture')