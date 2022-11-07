import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
from Assets.Sidebar import sidebar
from Cases import Case1, Case2, Case3


st.title('Verificador de Grafo Euleriano')

st.write("""Este sistema serve para mostrar se um determinado grafo é
       euleriano ou não, e em caso positivo, mostrar o caminho euleriano.
       Navegue na barra lateral entre os casos de uso para ver exemplos.""")
sidebar()

if 'case' not in st.session_state:
    st.session_state['case'] = 'case1'

if st.session_state['case'] == 'case1':
    Case1.case1()
if st.session_state['case'] == 'case2':
    Case2.case2()
if st.session_state['case'] == 'case3':
    Case3.case3()

