import streamlit as st
from uix.pages import about_page, home_page

#--- alt define sidebar pages
m_aryPages = {
    "Home":                         home_page,           #--- TODO:  update
    "About":                        about_page
}


#--- define module-level vars
m_aryDescr = [] 
m_aryMods = []


def init():
    #--- upper panel
    with st.sidebar:
        kstrUrl_image = "bin/images/logo.png"
        st.sidebar.image(kstrUrl_image, width=200)
        #st.sidebar.markdown('') 
 

    #--- init radio buttons
    strKey = st.sidebar.radio("", list(m_aryPages.keys()))
    pagSel = m_aryPages[strKey]
    writePage(pagSel)

def writePage(uixFile):  
    #--- writes out the page for the selected combo
  
    # _reload_module(page)
    uixFile.run()
