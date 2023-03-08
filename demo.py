import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt



st.set_page_config(page_title="DATA APP",
page_icon=':bar_chart:', layout="centered",
initial_sidebar_state="auto")

# title of the app 
st.title('COVID WORLD WIDE DATA VISUALISATION :bar_chart:')
st.subheader('the covid world wide statistics')
csv_file = 'covid_worldwide (1).csv'
sheet_name = 'DATA'

df_csv=pd.read_csv('covid_worldwide (1).csv')
df_csv

st.sidebar.header('Please Fiter Here:')
Country = st.sidebar._multiselect(
        'select the country:',
        options=df_csv['Country'].unique(),
        default=df_csv['Country'].unique()

)


country_data = pd.DataFrame({
    'country': ['USA', 'India', 'France' , 'Germany' ,'Brazil', 'Japan','S. Korea','Italy','UK','Russia'],
    'cases': [ 104196861 , 44682784, 39524311 , 37779833,36824580, 32588442, 30197066 ,25453789 , 24274361, 21958696],
    'total deaths':[ 104196861 , 44682784, 39524311 , 37779833,36824580, 32588442, 30197066 ,25453789 , 24274361, 21958696]
})
st.write("## Top 10  country")
# Create the bar chart using streamlit
st.bar_chart(country_data)

Data1 = [60,36,80]
labels=['Active Cases','Total test','Population']
explode=[0,0,0.2]

fig, ax = plt.subplots()
st.write("## Top 10  country totals")
ax.pie(Data1, labels=labels, colors=['green', 'yellow', 'red'], autopct='%.0f%%', shadow=True, explode=explode)
ax.set_title('')

st.pyplot(fig)

