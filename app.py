"""Simple app in streamlit"""
import streamlit as st
from area import circle

st.title("Welcome to My Streamlit App!")
st.write("This is a simple beginner-level Streamlit application.")

name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! 👋")

number = st.slider("Pick a number", 1, 100, 50)
st.write(f"You selected: {number}")

radius = st.number_input("Enter the radius of circle:")
if radius:
    st.write(circle(r=radius))

if st.button("Say Hello"):
    st.success("Hello Streamlit User!")
