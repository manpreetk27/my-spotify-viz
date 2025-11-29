import numpy as np
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

load_dotenv()

st.set_page_config(page_title="Top Artists", page_icon="🎤")

st.title(" 📯 my top artists")
st.markdown("here are my top 10 artists on spotify based on my listening habits!")
st.write("---")

if os.getenv("SPOTIFY_CLIENT_ID") and os.getenv("SPOTIFY_CLIENT_SECRET"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-top-read"
    ))
else:
    sp = None

try: # try to get real data
    results = sp.current_user_top_artists(limit=10) # fetch top 10 artists
    artist_names = [a['name'] for a in results['items']] # artist names
    artist_popularity = [a['popularity'] for a in results['items']] # artist popularity scores

except: # fallback data since my oauth might fail for others
    st.warning("⚠️ Spotify data can't be fetched — showing sample listening patterns instead. \n\nAdd your own Spotify credentials to see your top artists!")
    artist_names = ["Frank Ocean", "SZA", "Lorde", "Arctic Monkeys", "Tame Impala", "The Weeknd", "LANY", "Clairo", "Kali Uchis", "Post Malone"] # artist names
    artist_popularity = [95, 88, 83, 90, 87, 92, 78, 75, 80, 85] # artist popularity scores

# 3D figure setup
fig = plt.figure(figsize=(4, 3))  # smaller figure size
ax = fig.add_subplot(111, projection='3d') # this creates a 3D axis

# Transparent background for dark theme
fig.patch.set_alpha(0.0) # make figure background transparent
ax.set_facecolor('black') # set axis background to black

x = np.arange(len(artist_names)) # x positions
y = np.zeros_like(x) # y positions
z = np.zeros_like(x) # z positions (base of bars)

# make thinner bars
dx = np.ones_like(x) * 0.4 # bar width, multiplied by 0.4 to make thinner
dy = np.ones_like(x) * 0.4 # bar depth, multiplied by 0.4 to make thinner
dz = artist_popularity # bar heights

# use a smooth gradient palette
colors = plt.cm.plasma(np.linspace(0.3, 0.9, len(artist_names))) # plasma colormap from matplotlib

# plot
ax.bar3d(x, y, z, dx, dy, dz, color="hotpink", shade=True, zsort='average') # plot bars

# tilt the view for more dynamic look
ax.view_init(elev=25, azim=-65) # elevation and angle

# labels and style
ax.set_xticks(x) # set x ticks
ax.set_xticklabels(artist_names, rotation=45, ha='right', color='white', fontsize=7) # set x tick labels
ax.set_yticks([]) # hide y ticks
ax.set_zticks([0, 25, 50, 75, 100])
ax.set_zticklabels(['0', '25', '50', '75', '100'], color='white', fontsize=7) # z tick labels

ax.set_title("Manpreet's Top 10 Artists", fontsize=8, weight="bold", color='white') # title
ax.tick_params(colors='white') # tick parameters

# hide gridlines and panes for a smooth floating look
for spine in ax.spines.values(): # hide spines
    spine.set_visible(False) # hide spines

ax.xaxis.pane.fill = False # hide x axis pane
ax.yaxis.pane.fill = False # hide y axis pane
ax.zaxis.pane.fill = False # hide z axis pane

plt.tight_layout() # adjust layout
st.pyplot(fig) # display the figure
