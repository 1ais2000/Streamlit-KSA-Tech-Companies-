#--- about page
import streamlit as st

description = "About"

def run():

    print("\nINFO (about_page.run)  loading ", description, " page ...") 

    #--- 
    #st.experimental_memo.clear()            #--- try to clear cache each time this page is hit
    #st.cache_data.clear()

    st.markdown('### About')
    st.markdown('<style>.custom-link { text-decoration: none; color: #0000FF; }</style>', unsafe_allow_html=True)
    st.markdown('##### Credits (Project By): <a href="https://www.linkedin.com/in/aisha-y-7a8553139" class="custom-link">Aisha Yasir💻👩‍💻</a>', unsafe_allow_html=True)

    st.markdown('##### Disclaimer: ')
    st.markdown("The information on this web app is representative of the data scraped from the business directory site [https://www.saudiayp.com/](https://www.saudiayp.com/) and  for cybersecurity [https://elioplus.com/middle-east/saudi-arabia/channel-partners/data_security](https://elioplus.com/middle-east/saudi-arabia/channel-partners/data_security).")
    st.markdown("Hence, it **Does Not** represent **ALL** the technology companies in KSA within the 8 sectors of interest AND the details about the company name, location and sector is SAME as provided in these sites.")
    st.markdown(
        """
            About page
        """,
            unsafe_allow_html=True,
        )
    

