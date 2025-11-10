import streamlit as st
import pandas as pd
from utils import (merge_country_datasets, plot_solar_data_resampled, 
                   plot_monthly_solar_data, Heatmap, Scatter_Plots, 
                   Wind_rose, Hist_GHI, Bubble_chart, Boxplts_byCountry)

st.title('Solar Data Discovery')

# Load data
@st.cache_data
def load_data():
    df = merge_country_datasets()
    return df

df = load_data()

# Sidebar for navigation
st.sidebar.title('Navigation')
analysis_type = st.sidebar.radio('Choose Analysis Type', ['Country Comparison', 'Time Series Analysis', 'Correlation Analysis', 'Distribution Analysis'])

if analysis_type == 'Country Comparison':
    st.header('Country Comparison')
    figs = Boxplts_byCountry(df)
    for fig in figs:
        st.pyplot(fig)

elif analysis_type == 'Time Series Analysis':
    st.header('Time Series Analysis')
    fig1 = plot_solar_data_resampled(df)
    st.pyplot(fig1)
    fig2 = plot_monthly_solar_data(df)
    st.pyplot(fig2)

elif analysis_type == 'Correlation Analysis':
    st.header('Correlation Analysis')
    fig = Heatmap(df)
    st.pyplot(fig)
    figs = Scatter_Plots(df)
    for fig in figs:
        st.pyplot(fig)

elif analysis_type == 'Distribution Analysis':
    st.header('Distribution Analysis')
    fig1 = Wind_rose(df)
    st.pyplot(fig1)
    figs = Hist_GHI(df)
    for fig in figs:
        st.pyplot(fig)
    fig2 = Bubble_chart(df)
    st.pyplot(fig2)