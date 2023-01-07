#todo: generar ejemplo de simulacion
import pandas as pd

import contextlib, io

from execution import *

import streamlit as st
st.set_page_config(
        page_title="NDS",
        layout="wide",
        initial_sidebar_state="expanded",
    )


st.sidebar.title('NDS')
st.sidebar.markdown('Nations Development Simulator')

st.title('Nations Development Simulator')




col1, col2= st.columns([10,1])
with col1:
    code= st.text_area('code 1', placeholder='code here', height=200)
with col2:
    st.text('')
    st.text('')
    run= st.button('Run')

c= st.container()
if run:
    compiler= Code()
    
    try:
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            compiler.compile(code)
        output = f.getvalue()
        # c.text(output)
        # c.code(output)
        st.text_area('**Output**', height=200, value=output, disabled=True)
    except Exception as e:
        st.text_area('**Output**', height=100, value=e, disabled=True)
        
else:
    c.markdown('**Output**')