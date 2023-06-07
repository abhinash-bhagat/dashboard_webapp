import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import math

df = pd.read_excel('Datasets/store_sales.xlsx')
df_19 = df[df['Order Date'].dt.year == 2019]
df_20 = df[df['Order Date'].dt.year == 2020]


#Streamlit
st.set_page_config(layout="wide")
st.sidebar.image('logo.png')
st.markdown("""
        <h1 style="text-align: center;">BrainCatch Sales Dashboard</h1>
    """,unsafe_allow_html=True)
intro = st.markdown("""
        <h6 style="text-align: center;">Select the Year from the sidebar to visualize the Report and analyze it.</h6>
    """,unsafe_allow_html=True)

#**********************************************************************************************
#-----> For 2019<------------
#-----> Sales By Payment Mode <------
# Count the total number of items for each unique value in the 'Payment Mode' column
payment_mode_counts = df_19['Payment Mode'].value_counts()
# Create the labels for the pie chart using the index of the payment_mode_counts Series
labels = payment_mode_counts.index.tolist()
# Create the pie chart
fig = px.pie(values=payment_mode_counts, names=labels, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.RdBu)
# Set chart title
fig.update_layout(title_text='Sales By Payment Mode')


#-----> Sales By Region<------
# Count the total number of orders for each unique value in the 'Region' column
region_counts = df_19['Region'].value_counts()
# Create the labels for the pie chart using the index of the region_counts Series
labels_2 = region_counts.index.tolist()
# Create the pie chart
fig_2 = px.pie(values=region_counts, names=labels_2, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.RdBu)
# Set chart title
fig_2.update_layout(title_text='Sales By Regions')

#-----> Sales By Segment<------
# Count the total number of orders for each unique value in the 'Segment' column
segment_counts = df_19['Segment'].value_counts()
# Create the labels for the pie chart using the index of the segment_counts Series
labels_3 = segment_counts.index.tolist()
# Create the pie chart
fig_3 = px.pie(values=segment_counts, names=labels_3, hole=0.6,width=300 ,color_discrete_sequence=px.colors.sequential.RdBu)
# Set chart title
fig_3.update_layout(title_text='Sales By Segments')

#-----> Sales By Month<------
fig_4 = px.line(df_19, x='Order Date', y='Sales')
fig_4.update_traces(line_color='#f4a582')
fig_4.update_layout(title_text='Sales By Months')

#-----> Profit By Month<------
fig_5 = px.line(df_19, x='Order Date', y='Profit')
fig_5.update_traces(line_color='#f4a582')
fig_5.update_layout(title_text='Profit By Months')

#-----> Sales By Sub-Category<------
category_count = df_19['Sub-Category'].value_counts()
labels_4 = category_count.index.to_list()
fig_6 = go.Figure(go.Bar(
    x=category_count,
    y=labels_4,
    orientation='h'
))
fig_6.update_traces(marker_color='#f4a582')
fig_6.update_layout(title_text='Sales By Sub-Categories')

#**********************************************************************************************

#-----> For 2020<------------
#-----> Sales By Payment Mode <------
# Count the total number of items for each unique value in the 'Payment Mode' column
payment_mode_counts_b1 = df_20['Payment Mode'].value_counts()
# Create the labels for the pie chart using the index of the payment_mode_counts Series
labels_b1 = payment_mode_counts_b1.index.tolist()
# Create the pie chart
fig_b1 = px.pie(values=payment_mode_counts_b1, names=labels_b1, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.Electric_r)
# Set chart title
fig_b1.update_layout(title_text='Sales By Payment Mode')


#-----> Sales By Region<------
# Count the total number of orders for each unique value in the 'Region' column
region_counts_b2 = df_20['Region'].value_counts()
# Create the labels for the pie chart using the index of the region_counts Series
labels_b2 = region_counts_b2.index.tolist()
# Create the pie chart
fig_b2 = px.pie(values=region_counts_b2, names=labels_b2, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.Electric_r)
# Set chart title
fig_b2.update_layout(title_text='Sales By Regions')

#-----> Sales By Segment<------
# Count the total number of orders for each unique value in the 'Segment' column
segment_counts_b3 = df_20['Segment'].value_counts()
# Create the labels for the pie chart using the index of the segment_counts Series
labels_b3 = segment_counts_b3.index.tolist()
# Create the pie chartb
fig_b3 = px.pie(values=segment_counts_b3, names=labels_b3, hole=0.6,width=300 ,color_discrete_sequence=px.colors.sequential.Electric_r)
# Set chart title
fig_b3.update_layout(title_text='Sales By Segments')

#-----> Sales By Month<------
fig_b4 = px.line(df_20, x='Order Date', y='Sales')
fig_b4.update_traces(line_color='#e6c800')
fig_b4.update_layout(title_text='Sales By Months')

#-----> Profit By Month<------
fig_b5 = px.line(df_20, x='Order Date', y='Profit')
fig_b5.update_traces(line_color='#e6c800')
fig_b5.update_layout(title_text='Profit By Months')

#-----> Sales By Sub-Category<------
category_count_b6 = df_20['Sub-Category'].value_counts()
labels_b6 = category_count_b6.index.to_list()
fig_b6 = go.Figure(go.Bar(
    x=category_count_b6,
    y=labels_b6,
    orientation='h'
))
fig_b6.update_traces(marker_color='#e6c800')
fig_b6.update_layout(title_text='Sales By Sub-Categories')

#**********************************************************************************************

#-----> For Combined<------------
#-----> Sales By Payment Mode <------
# Count the total number of items for each unique value in the 'Payment Mode' column
payment_mode_counts_c1 = df['Payment Mode'].value_counts()
# Create the labels for the pie chart using the index of the payment_mode_counts Series
labels_c1 = payment_mode_counts_c1.index.tolist()
# Create the pie chart
fig_c1 = px.pie(values=payment_mode_counts_c1, names=labels_c1, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.Magenta_r)
# Set chart title
fig_c1.update_layout(title_text='Sales By Payment Mode')


#-----> Sales By Region<------
# Count the total number of orders for each unique value in the 'Region' column
region_counts_c2 = df['Region'].value_counts()
# Create the labels for the pie chart using the index of the region_counts Series
labels_c2 = region_counts_c2.index.tolist()
# Create the pie chart
fig_c2 = px.pie(values=region_counts_c2, names=labels_c2, hole=0.6,width=280 ,color_discrete_sequence=px.colors.sequential.Magenta_r)
# Set chart title
fig_c2.update_layout(title_text='Sales By Regions')

#-----> Sales By Segment<------
# Count the total number of orders for each unique value in the 'Segment' column
segment_counts_c3 = df['Segment'].value_counts()
# Create the labels for the pie chart using the index of the segment_counts Series
labels_c3 = segment_counts_c3.index.tolist()
# Create the pie chartb
fig_c3 = px.pie(values=segment_counts_c3, names=labels_c3, hole=0.6,width=300 ,color_discrete_sequence=px.colors.sequential.Magenta_r)
# Set chart title
fig_c3.update_layout(title_text='Sales By Segments')

#-----> Sales By Month<------
fig_c4 = px.line(df, x='Order Date', y='Sales')
fig_c4.update_traces(line_color='#ca699d')
fig_c4.update_layout(title_text='Sales By Months')

#-----> Profit By Month<------
fig_c5 = px.line(df, x='Order Date', y='Profit')
fig_c5.update_traces(line_color='#ca699d')
fig_c5.update_layout(title_text='Profit By Months')

#-----> Sales By Sub-Category<------
category_count_c6 = df['Sub-Category'].value_counts()
labels_c6 = category_count_c6.index.to_list()
fig_c6 = go.Figure(go.Bar(
    x=category_count_c6,
    y=labels_c6,
    orientation='h'
))
fig_c6.update_traces(marker_color='#ca699d')
fig_c6.update_layout(title_text='Sales By Sub-Categories')

#**********************************************************************************************
#Sidebar
if st.sidebar.button('2019'):
    st.markdown("""
        <h1 style="text-align: center;margin-bottom: 30px;">Year 2019 Report</h1>
    """,unsafe_allow_html=True)
    
    intro.empty()  # Empty text to hide the message

    #Streamlit 4 Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Orders", value=df_19['Order ID'].count(), delta=-174)
    col2.metric(label="Sales", value=math.floor(df_19['Sales'].sum()), delta=-38106)
    col3.metric(label="Profit", value=math.floor(df_19['Profit'].sum()), delta=-5689)
    col4.metric(label="Avg. Shipping Duration", value=('4-5'), delta=0)

    #Streamlit 6 Charts
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig)
    with col1:
        st.plotly_chart(fig_2)
    with col1:
        st.plotly_chart(fig_3)
    with col2:
        st.plotly_chart(fig_4)
    with col2:
        st.plotly_chart(fig_5)
    with col2:
        st.plotly_chart(fig_6)

#**********************************************************************************************
if st.sidebar.button('2020'):
    st.markdown("""
        <h1 style="text-align: center;margin-bottom: 30px;">Year 2020 Report</h1>
    """,unsafe_allow_html=True)

    intro.empty()  # Empty text to hide the message

    #Streamlit 4 Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Orders", value=df_20['Order ID'].count(), delta=int(df_20['Order ID'].count()-df_19['Order ID'].count()))
    col2.metric(label="Sales", value=math.floor(df_20['Sales'].sum()), delta=int(math.floor(df_20['Sales'].sum())-math.floor(df_19['Sales'].sum())))
    col3.metric(label="Profit", value=math.floor(df_20['Profit'].sum()), delta=int(math.floor(df_20['Profit'].sum())-math.floor(df_19['Profit'].sum())))
    col4.metric(label="Avg. Shipping Duration", value=('4-5'), delta=0)

    #Streamlit 6 Charts
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig_b1)
    with col1:
        st.plotly_chart(fig_b2)
    with col1:
        st.plotly_chart(fig_b3)
    with col2:
        st.plotly_chart(fig_b4)
    with col2:
        st.plotly_chart(fig_b5)
    with col2:
        st.plotly_chart(fig_b6)

#**********************************************************************************************
if st.sidebar.button('Combined'):
    st.markdown("""
        <h1 style="text-align: center;margin-bottom: 30px;">2019-2020 Report</h1>
    """,unsafe_allow_html=True)

    intro.empty()  # Empty text to hide the message

    #Streamlit 4 Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Orders", value=df['Order ID'].count(), delta=0)
    col2.metric(label="Sales", value=math.floor(df['Sales'].sum()), delta=0)
    col3.metric(label="Profit", value=math.floor(df['Profit'].sum()), delta=0)
    col4.metric(label="Avg. Shipping Duration", value=('4-5'), delta=0)

    #Streamlit 6 Charts
    col1, col2, col3 = st.columns(3)
    with col1:
        st.plotly_chart(fig_c1)
    with col1:
        st.plotly_chart(fig_c2)
    with col1:
        st.plotly_chart(fig_c3)
    with col2:
        st.plotly_chart(fig_c4)
    with col2:
        st.plotly_chart(fig_c5)
    with col2:
        st.plotly_chart(fig_c6)


#--------------------------------> Custom CSS <-----------------------------------------------
st.markdown("""
    <style>
    .css-6qob1r {
        background-color: #2c2c2c;
    }
    .css-ocqkz7{
        margin-bottom: 30px;
    }
    .css-fblp2m{
        color: white;
    }
    </style>
""",unsafe_allow_html=True)
