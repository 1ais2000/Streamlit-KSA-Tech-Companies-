import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Define sections
sections = {
    "INTRODUCTION": "Home",
    "DATA_VISUALIZATION": "Data Visualization",
    "TABLE_DISPLAY": "Companies by Sector and Location",
}

# Section: INTRODUCTION
@st.cache_data
def load_data():
    # Load CSV dataset
    data = pd.read_csv('./bin/files/updated_tech_companies_in_KSA.csv')

    # Replace "<NA>" string with NaN values in the "location" column
    data['location'] = data['location'].replace('<NA>', np.nan)

    # Remove rows with NaN values in the "location" column
    data = data.dropna(subset=['location'])

    # Keep only one row for each unique company name and remove duplicates
    data = data.drop_duplicates(subset='company_name')

    return data

def introduction_section():
    st.markdown('### Home')
    st.markdown("#### Background ")
    st.markdown("<p class='text-justify'>In this web page, we dive into the thriving technology industry of KSA. Here, you will find a comprehensive list of technology companies operating in various sectors within KSA" 
                 ". Our goal is to provide you with valuable insights into the technology landscape of KSA, enabling you to explore the" 
                 " diverse sectors within the industry.  Whether you are a student, professional, or technology enthusiast, this web page is"
                   " your gateway to discover and navigate the vibrant tech ecosystem of KSA. <p> ", unsafe_allow_html=True)
    st.markdown("<p class='text-justify'>💡 From a student perspective, this project is an exciting opportunity! It opens doors for students interested in pursuing internships within the technology industry. By leveraging the scraped information, students can make informed decisions about their internship choices, ensuring a perfect fit for their aspirations and goals.</p>", unsafe_allow_html=True)
    st.markdown("<p class='text-justify'>🔍Students can explore various sectors within the technology industry in KSA.</p>",  unsafe_allow_html=True)
    st.markdown("<p class='text-justify'>The objective of this web app is to present and visualize the data scraped using **BeautifulSoup** 📊.🚀.In the web scraping, the aim was to gather data on the company name, industry/sector, and location for technology (CS) companies in 8 technology industry sectors. The data was scarped from the companies <a href= https://www.saudiayp.com/ > business directory website </a>  and <a href= https://elioplus.com/middle-east/saudi-arabia/channel-partners/data_security > this site for cybersecurity companies</a>and was used to  create a comprehensive list of tech companies operating in KSA in 7 sectors:  </p>",  unsafe_allow_html=True)
    st.markdown("- 🌐 Web Hosting\n- 💻 Information Technology\n- 🌐 Web Development\n- 🎨 Web Designers\n- 📱 Software Applications\n- 💾 Computer Software Solution\n- 🖥️ Computer Services,\n- 🛡️ CyberSecurity")
    st.markdown('###### Project done by: Aisha Yasir')

# Section: DATA_VISUALIZATION
def data_visualization_section(data):
    st.markdown('### Data Visualization')
    visualization_option = st.selectbox('Select visualization option:', ('No. Of Companies by Sector', 'No. Of Companies by Location'))

    if visualization_option == 'No. Of Companies by Sector':
        sector_counts = data['sector'].value_counts()
        fig_sector_counts = px.bar(x=sector_counts.index, y=sector_counts.values, labels={'x': 'Sector', 'y': 'Count'}, color=sector_counts.index)  
        fig_sector_counts.update_layout(yaxis_range=[0, max(sector_counts.values) + 10])  
        st.plotly_chart(fig_sector_counts)

    elif visualization_option == 'No. Of Companies by Location':
        location_counts = data['location'].value_counts()
        fig_location_counts = px.bar(x=location_counts.index, y=location_counts.values, labels={'x': 'Location', 'y': 'Count'}, color=location_counts.index)  
        fig_location_counts.update_layout(yaxis_range=[0, max(location_counts.values) + 10])  
        st.plotly_chart(fig_location_counts)

# Section: TABLE_DISPLAY
def table_display_section(data):
    st.markdown('### Companies by Sector and Location')

    selected_sector = st.selectbox('Select a sector:', ['All'] + list(data['sector'].unique()))
    selected_location = st.selectbox('Select a location:', ['All'] + list(data['location'].unique()))

    if selected_sector == "All" and selected_location == "All":
        selected_data = data[['company_name', 'sector', 'location']]
        st.table(selected_data)
    elif selected_sector == "All":
        selected_data = data[(data['location'] == selected_location)][['company_name', 'sector', 'location']]
        st.table(selected_data)
    elif selected_location == "All":       
        selected_data = data[(data['sector'] == selected_sector)][['company_name', 'sector', 'location']]
        st.table(selected_data)
    else:
        selected_data = data[(data['sector'] == selected_sector) & (data['location'] == selected_location)][['company_name', 'sector', 'location']]
        st.table(selected_data)

# Main function
def run():
    st.markdown(
        """
        <style>
        .text-justify {
            text-align: justify;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    print("\nINFO (lit_home.run)  loading ", sections["INTRODUCTION"], " page ...")

    # Load data using caching
    data = load_data()

    # INTRODUCTION SECTION
    introduction_section()

    # DATA VISUALIZATION SECTION
    data_visualization_section(data)

    # TABLE DISPLAY SECTION 
    table_display_section(data)

    st.markdown(
        """
        Home page
        """,
        unsafe_allow_html=True,
    )



