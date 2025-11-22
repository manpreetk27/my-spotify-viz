import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pandas as pd # data manipulation
import plotly.graph_objects as go # for creating plots
import numpy as np # numerical operations
import plotly.express as px  # for color scales

# page setup
st.set_page_config(page_title="My Genre Galaxy", page_icon="🌌", layout="centered")
st.title("🌌 my genre galaxy")
st.write("each genre plotted as an orbiting planet though space - based on my top artists' genres")

# spotify auth
load_dotenv()

# Only initialize Spotify if credentials exist
if os.getenv("SPOTIFY_CLIENT_ID") and os.getenv("SPOTIFY_CLIENT_SECRET"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-top-read"
    ))
else:
    sp = None

# fetch genres 
try: # try to get real data
    data = sp.current_user_top_artists(limit=50) # fetch top artists
    raw_genres = [] # collect genres
    for artist in data.get("items", []): # iterate artists
        g = artist.get("genres", []) # get genres
        if g: # if genres exist
            raw_genres.append(g[0]) # take primary genre
    if not raw_genres: # no genres fetched
        raise Exception("no genres fetched") # trigger except block
    genre_counts = pd.Series(raw_genres).value_counts().head(12) # top 12 genres
    df = pd.DataFrame({"genre": genre_counts.index, "count": genre_counts.values}) # dataframe
except: # fallback data
    df = pd.DataFrame({ # dummy data
        "genre": ["indie pop", "bedroom pop", "electropop", "alt-pop", "lo-fi", "synthwave", "r&b", "indie rock"], # genres
        "count": [18, 14, 12, 10, 8, 6, 5, 4] # counts
    })

# spiral coordinates
df["angle"] = np.linspace(0, 4 * np.pi, len(df))  # spiral angle is "how far around the circle each genre is", linspace does this evenly
df["radius"] = np.linspace(0.2, 1, len(df)) * df["count"] / df["count"].max()  # radius is "distance from center", scaled by count
df["x"] = df["radius"] * np.cos(df["angle"]) # convert to cartesian which means x and y coordinates
df["y"] = df["radius"] * np.sin(df["angle"]) # convert to cartesian which means x and y coordinates

# plasma neon colors
colors = px.colors.sequential.Plasma # use plotly's plasma color scale
vals = np.linspace(0, len(colors)-1, len(df)) # map genre count to color index
df["color"] = [colors[int(v)] for v in vals] # assign colors

# plot
fig = go.Figure() # create figure

fig.add_trace(go.Scatter( # scatter plot
    x=df["x"], y=df["y"], # x and y coordinates
    mode="markers+text", # markers and text
    marker=dict(
        size=df["count"] * 2 + 10,  # this is the size of each planet, scaled up for visibility, multiplied by 2 and offset by 10 which makes even small counts visible
        color=df["color"], # color from plasma scale
        opacity=0.9, # slight transparency
    ),
    text=df["genre"], # genre labels
    textposition="top center", # position labels above markers
    hovertemplate="<b>%{text}</b><br>count: %{marker.size}<extra></extra>" # hover info
))

fig.update_layout( # layout settings
    paper_bgcolor="black", # black background
    plot_bgcolor="black", # black plot area
    showlegend=False, # no legend
    xaxis=dict(visible=False), # hide x-axis
    yaxis=dict(visible=False), # hide y-axis
    margin=dict(l=0, r=0, t=20, b=20), # tight margins
)

st.plotly_chart(fig, use_container_width=True) # display plot in streamlit

# insight
top_genre = df.iloc[0]["genre"] # most frequent genre iloc gets first row from dataframe
st.subheader("🔭 quick decode")
st.markdown(f"my core sound orbits around **{top_genre}** — the brightest planet in my galaxy.")

