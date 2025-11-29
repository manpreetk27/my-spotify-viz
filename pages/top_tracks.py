import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pandas as pd
import plotly.express as px

# Load environment variables
load_dotenv()

if os.getenv("SPOTIFY_CLIENT_ID") and os.getenv("SPOTIFY_CLIENT_SECRET"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-top-read"
    ))
else:
    sp = None

st.set_page_config(page_title="Top Tracks", page_icon="🎵", layout="wide")

st.title(" 🏆 my top spotify tracks")
st.write("An interactive look into my most-played songs!")

try: # try to get real data
    # Fetch top tracks
    results = sp.current_user_top_tracks(limit=15) # fetch top 15 tracks
    tracks = results['items'] # extract track items

    # Extract data
    track_names = [t['name'] for t in tracks] # track names
    artists = [t['artists'][0]['name'] for t in tracks] # primary artist names
    popularities = [t['popularity'] for t in tracks] # track popularity scores
    durations = [t['duration_ms'] / 1000 / 60 for t in tracks]  # convert ms to minutes

except: # fallback data since my oauth might fail for others
    st.warning("⚠️ Since Manpreet's Spotify data can't be fetched — showing sample listening patterns instead! Add your own Spotify credentials to see your top tracks!")
    track_names = ["Pink + White", "Cool With You", "Supercut", "505", "Nights", "Die For You", "Golden Hour", "Kill Bill", "Electric Feel", "ILYSB"]
    artists = ["Frank Ocean", "NewJeans", "Lorde", "Arctic Monkeys", "Frank Ocean", "The Weeknd", "JVKE", "SZA", "MGMT", "LANY"]
    popularities = [95, 90, 87, 89, 92, 94, 88, 85, 86, 84]
    durations = [3.5, 2.8, 3.2, 3.8, 4.0, 3.9, 3.1, 2.9, 4.2, 3.7]

df = pd.DataFrame({
    "Track": track_names, # track names
    "Artist": artists, # primary artist names
    "Popularity": popularities, # track popularity scores
    "Duration (min)": durations # duration in minutes
})

# Interactive plot
fig = px.scatter( # scatter plot
    df,
    x="Duration (min)",
    y="Popularity",
    text="Track",
    color="Popularity",
    color_continuous_scale=px.colors.sequential.Plasma, # plasma color scale
    hover_data=["Artist"], # hover info
    title="Popularity vs Duration of My Top Tracks",
    height=600  # set graph height larger
)

fig.update_traces(textposition="top center", marker=dict(size=14, line=dict(width=1, color='white'))) # marker style
fig.update_layout( # layout settings
    plot_bgcolor="rgba(0,0,0,0)", # transparent background
    paper_bgcolor="rgba(0,0,0,0)", # transparent background
    font=dict(color="white", size=12), # font settings
    title_font=dict(size=18, color="white", family="Arial Black") # title font settings
)

st.plotly_chart(fig, use_container_width=True) # display plot

st.subheader("Track Details")
st.dataframe(df) # display dataframe
