import streamlit as st
import pandas as pd

st.title('Descriptive Stats GUI')

with st.sidebar:
    st.title('Insert your file here')
    st.file_uploader('CSV numbers', 'csv')



