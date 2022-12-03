from GraphGenerator import graph_generator
from Assets.Buttons import button_for_check
from Assets.Buttons import button_for_path
import streamlit as st

def case1():
    matrix = [
                [0, 1, 0, 0],
                [1, 0, 0, 1],
                [0, 0, 0, 1],
                [0, 1, 1, 0]
            ]

    col1, col2 = st.columns(2)
    with col1:
        graph_generator(matrix)

    with col2:
        st.header("Matriz de adjacências utilizada")
        st.latex(r""" \begin{bmatrix}
                0 & 1 & 0 & 0 \\
                1 & 0 & 0 & 1 \\
                0 & 0 & 0 & 1 \\
                0 & 1 & 1 & 0 
                \end{bmatrix}  
                """)
        button_for_check(matrix)
        button_for_path(matrix)