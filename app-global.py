import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
@st.cache_data
def load_data():
    return pd.read_csv('Global-Air-Pollution-Data.csv')

def main():

    # Title and description
    st.title('Visualisasi Data Polusi Udara Global')
    st.write('Menganalisis dataset untuk deteksi Polusi Udara')

    # Load the data
    data = load_data()

    # Sidebar
    st.sidebar.title('Options')

    # Select features for visualization
    selected_feature_hist = st.sidebar.selectbox('Select Feature for Histogram', data.columns)
    selected_feature_scatter_x = st.sidebar.selectbox('Select Feature for Scatter Plot X-axis', data.columns)
    selected_feature_scatter_y = st.sidebar.selectbox('Select Feature for Scatter Plot Y-axis', data.columns)

     # Display the dataset
    st.subheader('Raw Data')
    st.write(data)


    # Histogram for selected feature
    st.subheader(f'Histogram for {selected_feature_hist}')
    fig_hist = px.histogram(data, x=selected_feature_hist, title=f'Histogram for {selected_feature_hist}')
    st.plotly_chart(fig_hist)

    # Scatter plot for selected features
    st.subheader(f'Scatter Plot for {selected_feature_scatter_x} vs {selected_feature_scatter_y}')
    fig_scatter = px.scatter(data, x=selected_feature_scatter_x, y=selected_feature_scatter_y, title=f'{selected_feature_scatter_x} vs {selected_feature_scatter_y}')
    st.plotly_chart(fig_scatter)

    # Correlation heatmap
    st.subheader('Correlation Heatmap')
    numeric_cols = data.select_dtypes(include='number').columns.tolist()
    corr = data[numeric_cols].corr()
    fig_corr = go.Figure(data=go.Heatmap(z=corr.values, x=corr.index, y=corr.columns, colorscale='Viridis'))
    fig_corr.update_layout(width=800, height=600, title='Correlation Heatmap')
    st.plotly_chart(fig_corr)

   
if __name__ == "__main__":
    main()
