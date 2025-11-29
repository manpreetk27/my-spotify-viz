import streamlit as st # web app framework
import spotipy # spotify API client
from spotipy.oauth2 import SpotifyOAuth # OAuth for Spotify
import pandas as pd # data manipulation
import matplotlib.pyplot as plt # plotting
import seaborn as sns # statistical data visualization
import numpy as np # numerical operations
import os
from dotenv import load_dotenv

# streamlit page setup
st.set_page_config(page_title="Listening Habits", page_icon="🎧", layout="centered")
st.title("🕓 my listening habits")
st.write("A visual timeline of when I listen the most - based on my Spotify activity!")

# spotify authentication
load_dotenv()

if os.getenv("SPOTIFY_CLIENT_ID") and os.getenv("SPOTIFY_CLIENT_SECRET"):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
        scope="user-read-recently-played user-top-read"
    ))
else:
    sp = None

try:
    recent_tracks = sp.current_user_recently_played(limit=50)["items"]  # fetch recent tracks
    if not recent_tracks:  # no recent tracks found
        st.warning("No recent listening data found. Try playing some songs and refresh!")
        raise ValueError("No recent listening data.") # trigger except block
    
    # extract play timestamps
    df = pd.DataFrame({ # create dataframe
        "played_at": pd.to_datetime([t["played_at"] for t in recent_tracks], format='ISO8601') # convert to datetime
    })

    # convert UTC to local time (Malaysia Time)
    df["played_at"] = df["played_at"].dt.tz_convert("Asia/Kuala_Lumpur")

    # extract day and 12-hour format hour
    df["hour"] = df["played_at"].dt.strftime("%I %p")  # e.g., 03 PM
    df["day"] = df["played_at"].dt.day_name() # e.g., Monday

except Exception as e: # fallback to sample data
    st.warning(f"⚠️ Spotify data can't be fetched — showing sample listening patterns instead. \n\nAdd your own Spotify credentials to see your personal listening patterns!")
    # Simulated sample data to still render the visualisation
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # days of the week
    hours = [f"{(h if h != 0 else 12):02d} AM" if h < 12 else f"{(h-12 if h != 12 else 12):02d} PM" for h in range(24)]
    np.random.seed(42) # for reproducibility
    df = pd.DataFrame({ # create sample dataframe
        "day": np.random.choice(days_order, 80), # random days
        "hour": np.random.choice(hours, 80) # random hours
    })

# Proceed with visualization regardless (real or sample data)
days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # days of the week
df["day"] = pd.Categorical(df["day"], categories=days_order, ordered=True) # order days
heatmap_data = df.groupby(["day", "hour"]).size().unstack(fill_value=0) # pivot table
heatmap_data = heatmap_data.reindex(columns=sorted(heatmap_data.columns, key=lambda x: pd.to_datetime(x, format="%I %p"))) # order hours

plt.style.use("dark_background") # dark theme
fig, ax = plt.subplots(figsize=(10, 5)) # figure size
sns.heatmap( # heatmap
    heatmap_data, # data
    cmap="coolwarm", # color map
    linewidths=0.4, # line widths
    linecolor="black", # line color
    cbar_kws={"label": "Songs Played"}, # color bar label
    ax=ax # axis
)

ax.set_title("When I Listen Most", fontsize=15, weight="bold", color="white", pad=15) # title
ax.set_xlabel("Time of Day", color="white") # x-axis label
ax.set_ylabel("Day of Week", color="white") # y-axis label
ax.tick_params(colors="white", labelsize=9) # tick parameters

st.pyplot(fig) # display plot
st.caption("""
**How to read this:**  
Each square represents how many songs were played during a specific hour on a given day.  
- 🔥 Brighter colors = more listening activity  
- 🌙 Darker colors = quieter listening times  
- 🕐 Time shown in 12-hour format  
""")
