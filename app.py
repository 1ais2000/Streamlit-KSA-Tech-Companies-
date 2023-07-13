'''
    toExecute:  (from root app folder) ... streamlit run app.py
'''

import streamlit as st
import lit_sidebar as litSideBar

st.set_page_config(
    page_title="Technology companies in KSA",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "# A web app to explore tech(CS) companies in your region and prefered sector (scraped from business directory website)!"
    }
)


st.header("Technology companies in KSA 🖥️")
st.markdown('---')
#--- streamlit:  add a sidebar 
litSideBar.init()

