import streamlit as st
import math

st.header("Simple Maths")

choices = ['Area of Square','Area of Circle']

choice = st.radio('select option', choices)

if choice == choice[0]:
    side = st.number_input("length of a side", min_value=1, max_value=100)
    area = side**2
    st.success(f'The total area is = {area:.2f}')

if choice == choice[1]:
    side = st.number_input("radius of circle", min_value=1, max_value=1000)
    area = math.pi * r ** 2
    st.success(f'The total area is = {area:.2f}')