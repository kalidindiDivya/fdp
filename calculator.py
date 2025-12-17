import streamlit as st

st.title("Calculator")
st.write("This is a simple calculator app.")

col1, col2 = st.columns(2)
with col1:
	a = st.number_input("First number", value=0.0, format="%f")
with col2:
	b = st.number_input("Second number", value=0.0, format="%f")

if st.button("Add"):
	result = a + b
	st.markdown(f"<p style='color:blue; font-weight:600;'>Result: {result}</p>", unsafe_allow_html=True)