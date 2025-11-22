# note: this page uses simulated data for visualisation (no Spotify API required) - done because of API limitations
import streamlit as st # streamlit for web app
import pandas as pd # data manipulation
import numpy as np # numerical operations
import plotly.express as px # interactive plotting
import matplotlib.pyplot as plt # for static plotting

st.set_page_config(page_title="Aura Visualiser", page_icon="🌈", layout="centered")
st.title(" 🌻 my spotify aura")
st.write("An interactive visualisation of my music mood — inspired by Spotify Wrapped’s emotional color palette 🎶")

# simulated song data with energy, valence, danceability
data = {
    "Track": [
        "Pink + White", "Cigarette Daydreams", "Golden Hour", "The Less I Know The Better", "Supercut",
        "Kill Bill", "505", "Nights", "Die For You", "Electric Feel", "Cool With You", "Lover Is A Day",
        "Some", "ILYSB", "Bags", "After Dark", "Moonlight", "Sunflower", "Blue Lights", "Borderline"
    ],
    "Artist": [
        "Frank Ocean", "Cage The Elephant", "JVKE", "Tame Impala", "Lorde", "SZA", "Arctic Monkeys",
        "Frank Ocean", "The Weeknd", "MGMT", "NewJeans", "Cuco", "Soyou", "LANY", "Clairo",
        "Mr.Kitty", "Kali Uchis", "Post Malone", "Jorja Smith", "Tame Impala"
    ]
}

np.random.seed(42) # for reproducible random values
data["Energy"] = np.random.uniform(0.4, 1.0, 20) # what this does is randomly assigns energy levels
data["Valence"] = np.random.uniform(0.2, 1.0, 20) # what this does is randomly assigns emotional positivity
data["Danceability"] = np.random.uniform(0.3, 1.0, 20) # what this does is randomly assigns danceability
df = pd.DataFrame(data) # create dataframe

# plotly aura visual
fig = px.scatter( # interactive scatter plot
    df,
    x="Danceability", # x-axis is danceability
    y="Energy", # y-axis is energy
    size="Energy", # size of points based on energy
    color="Valence", # color based on valence
    color_continuous_scale="plasma", # color scale, plasma is for vibrant colors
    hover_name="Track", # hover text shows track name
    hover_data={ # additional hover data
        "Artist": True, # shows artist name
        "Energy": ":.2f", # format energy to 2 decimal places
        "Valence": ":.2f", # format valence to 2 decimal places
        "Danceability": ":.2f", # format danceability to 2 decimal places
    },
    title="my musical aura", # plot title
    size_max=60, # maximum size of points
    height=700,  # increase plot height
)

fig.update_layout( # layout adjustments
    paper_bgcolor="black", # background color of the paper which is the area around the plot
    plot_bgcolor="black", # background color of the plot
    font=dict(color="white"), # font color
    title_font=dict(size=22, color="white"), # title font size and color
    xaxis=dict(title="Danceability →", color="white", gridcolor="rgba(255,255,255,0.1)"), # x-axis settings
    yaxis=dict(title="↑ Energy", color="white", gridcolor="rgba(255,255,255,0.1)"), # y-axis settings
)

st.plotly_chart(fig, use_container_width=True) # display plot in streamlit

# mood color scale
st.subheader("🎨 Aura Color Scale – What the Colors Mean") 

gradient = np.linspace(0, 1, 256) # this creates a gradient from 0 to 1, linspace generates evenly spaced values
gradient = np.vstack((gradient, gradient)) # stack to make it 2D for imshow which is used for displaying images

fig2, ax2 = plt.subplots(figsize=(9, 1)) # create a wide, short figure for the color scale
ax2.imshow(gradient, aspect='auto', cmap='plasma') # display the gradient with plasma colormap
ax2.set_axis_off() # hide axes
fig2.patch.set_facecolor('black')  # set figure bg to black
ax2.set_facecolor('black')         # set axis bg to black
st.pyplot(fig2) # display the color scale in streamlit

st.markdown("""
| **Color** | **Mood Meaning** |
|------------|------------------|
| 💜 Deep Violet | Reflective, moody, introspective |
| 💗 Pink | Emotional, romantic, dreamy |
| 🧡 Orange | Energetic, confident, passionate |
| 💛 Yellow | Joyful, bright, upbeat |
""")

# data table
st.subheader("🪩 My Aura Breakdown (Simulated)") 
st.dataframe(df.style.format({
    "Energy": "{:.2f}", "Valence": "{:.2f}", "Danceability": "{:.2f}" # format to 2 decimal places
}).background_gradient(cmap='plasma', subset=["Energy", "Valence", "Danceability"])) # apply plasma colormap gradient to specified columns

# description
st.markdown("""
Each dot represents a song 🎧  
- **Color** = emotional positivity (valence)  
- **Size** = energy level  
- **X/Y position** = how lively & danceable it feels  

Together, they form my **musical aura** — a glowing reflection of my vibe and energy
""")



