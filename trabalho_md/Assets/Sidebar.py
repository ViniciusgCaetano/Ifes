import streamlit as st
from Cases import Case1, Case2, Case3


def sidebar():    
    st.markdown("""
                    <style>
                        .css-629wbf{
                            width: 100%
                        }
                        
                        .css-2ykyy6 {
                            display: none;
                        }
                        
                        .css-hxt7ib{
                            padding-top: 2rem;
                        }
                        
                        
                    </style>
                    
                    
                """,unsafe_allow_html=True)

    st.sidebar.title("Verificador de Grafo Euleriano")
    if st.sidebar.button('Caso 1'):
        st.session_state['case'] = 'case1'

    if st.sidebar.button('Caso 2'):
        st.session_state['case'] = 'case2'

    if st.sidebar.button('Caso 3'):
        st.session_state['case'] = 'case3'
    
    if st.sidebar.button('Caso 4'):
        st.session_state['case'] = 'case4'
