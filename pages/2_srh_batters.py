import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os
import plotly.graph_objs as go
# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "Image", "srh_logo.png")
DATA_PATH = os.path.join(dir_of_interest, "Data", "srh_batters_last_3_years_data.csv")

st.title("Dashboard- SRH Batters 2023 Performances from last 3 years")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)
# Create a trace for the scatter plot
trace = go.Scatter(x = df["Avg"],y = df["SR"],mode='markers+text', text=df["Player"], textposition='top center')
trace_1 = go.Scatter(x = df["BPB"],y = df["BP6"],mode='markers+text', text=df["Player"], textposition='top center')
# Create the layout for the scatter plot
layout = go.Layout(title='SRH batters Avg and SR From last 3 years', 
                   xaxis=dict(title='Player Batting Average'), yaxis=dict(title='Player Batting Strike Rate'))
layout_1 = go.Layout(title='SRH batters BPB and BP6 From last 3 years', 
                   xaxis=dict(title='Player Balls Per Boundary'), yaxis=dict(title='Player Balls Per Six'))
col1,col2  = st.columns(2)


# Create the figure object that will hold the graph and the layout
fig_1 = go.Figure(data=[trace], layout=layout)
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = go.Figure(data=[trace_1], layout=layout_1)
col2.plotly_chart(fig_2, use_container_width=True)


