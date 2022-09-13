import streamlit as st

st.write("Hello, let's learn how to build streamlit app together")

st.title("Here is Zachary")

st.header("this is the header")

st.markdown("this is the markdown")

st.subheader("this is the subheader")

st.caption("this is the caption")

st.code("x=2021")

st.latex(r" 'a+a r^1+a r^2+2 r^3' ")

#如何通过submit收集数据
sentences1 = st.text_input('Insert sentences1:')
if st.button('reading data'):
  data = pd.read_csv('https://raw.githubusercontent.com/HamidBekamiri/Data_Science_Handbook/main/chipotle.csv')
  st.write(data)
