import streamlit as st

st.write("Hello, let's learn how to build streamlit app together")

st.title("Here is Zachary")

st.header("this is the header")

st.markdown("this is the markdown")

st.subheader("this is the subheader")

st.caption("this is the caption")

st.code("x=2021")

st.latex(r" 'a+a r^1+a r^2+2 r^3' ")

import altair as alt
import numpy as np
import pandas as pd

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x ** 2 + y ** 2

# Convert this grid to columnar data expected by Altair
source = pd.DataFrame({'x': x.ravel(),
                     'y': y.ravel(),
                     'z': z.ravel()})

c1=alt.Chart(source).mark_rect().encode(
    x='x:O',
    y='y:O',
    color='z:Q'
  
  
  
if st.button("reading data"):
  st,
)

st.altair_chart(c1, use_container_width=True)

sentences1 = st.text_input('Insert sentences1:')
if st.button('Submit'):
  data = pd.read_csv('https://raw.githubusercontent.com/HamidBekamiri/Data_Science_Handbook/main/chipotle.csv')
  st.write(data)


#如何通过submit收集数据
