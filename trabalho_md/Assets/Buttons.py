import streamlit as st
from IsEulerian import is_eulerian
from discover_path import discover_path


def button_for_check(matrix):
    st.markdown("""
                    <style>
                        .css-1x8cf1d{
                            width: 100%
                        }
                    </style>     
                """,unsafe_allow_html=True)
    if st.button('Checar se é Euleriano'):
        if is_eulerian(matrix):
            st.success('Esse grafo é euleriano!')
            
        else:
            st.error('Esse grafo não é euleriano!')

def button_for_path(matrix):
    if st.button('Ver caminho'):
        discover_path(matrix)
