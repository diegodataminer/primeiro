import streamlit as st
import pandas as pd

data = {
    'Series_1': [1,2,3,4],
    'Series_2': [10, 20, 30, 40]
}

df = pd.DataFrame(data)

st.title('our first streamlit app')
st.subheader('introducing streamlit')
st.write('''this is out firts web app
         enjoy!

         
         ''')
st.write(df)

st.line_chart(df)

st.area_chart(df)

myslider = st.slider('celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)