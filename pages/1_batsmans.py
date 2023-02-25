import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "Image", "ipl.jpg")
DATA_PATH = os.path.join(dir_of_interest, "Data", "last_3_t20s_batters_data.csv")

st.title("Dashboard- IPL Batters 2023 Performances from last 3 years")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

team_selected = st.selectbox("Select the Team:", df['Team'].unique())
team_data = df[df["Team"] == team_selected]
#player = st.selectbox("Select the Player:",team_data["Player"].unique())
col1,col2  = st.columns(2)

layout = go.Layout(title='Player Batting Average', xaxis=dict(title='Player Name'), yaxis=dict(title='Player Batting Average'))
layout_1 = go.Layout(title='Player Batting Strike Rate', xaxis=dict(title='Player Name'), yaxis=dict(title='Player Batting Strike Rate'))
col1, col2 = st.columns(2)
trace = go.Bar(x=team_data["Player"], y=team_data["Avg"])
fig_1 = go.Figure(trace,layout)
col1.plotly_chart(fig_1, use_container_width=True)


trace_1 = go.Bar(x=team_data["Player"], y=team_data["SR"])
fig_2 = go.Figure(trace_1,layout_1)
col2.plotly_chart(fig_2, use_container_width=True)