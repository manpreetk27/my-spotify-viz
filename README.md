# 🎧 Manpreet's Spotify Insights Dashboard


A personalized data visualization dashboard that transforms your Spotify listening habits into beautiful, interactive charts and insights. Built with Streamlit, Plotly, and the Spotify API.

---
<img width="1500" height="440" src="https://github.com/manpreetk27/my-spotify-viz/blob/0c3c87a76e76222b29c87d3f52bd0fd4f2d881bb/assets/screen.png"/>

## ✨ Features

- **🌌 Genre Galaxy** — Visualize your top 12 genres as orbiting planets in an interactive spiral
- **🎤 Top Artists** — See your favorite artists in an eye-catching 3D bar chart
- **🎵 Top Tracks** — Explore your most-played songs with popularity vs. duration analysis
- **🕓 Listening Habits** — Discover when you listen the most with a day-of-week heatmap
- **🌈 Aura Visualizer** — Experience your musical mood through an interactive energy-valence scatter plot

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Spotify Developer Account (for real data)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Spotify

2. **Create a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Create a `.env` file with your Spotify API credentials (optional for demo)**
    ```bash
    SPOTIFY_CLIENT_ID= your_client_id
    SPOTIFY_CLIENT_SECRET= your_client_secret
    SPOTIFY_REDIRECT_URI= http://127.0.0.1:8888/callback

5. **Run the dashboard**
    ```bash
    streamlit run spotify_dashboard.py

## 🔑 Getting Spotify API Credentials

1. Go to Spotify Developer Dashboard
2. Log in or create a Spotify account
3. Create a new app
4. Accept the terms and create the app
5. Copy your Client ID and Client Secret
6. Add `http://127.0.0.1:8888/callback` as a Redirect URI
7. Paste these into your `.env` file

## 📁 Project Structure
    
    Spotify/
    ├── spotify_dashboard.py          # Main entry point
    ├── pages/
    │   ├── my_spotify_insights.py    # Genre Galaxy visualization
    │   ├── top_artists.py            # 3D artists chart
    │   ├── top_tracks.py             # Tracks analysis
    │   ├── listening_habits.py       # Listening heatmap
    │   └── aura_visualizer.py        # Musical mood visualization
    ├── .streamlit/
    │   └── config.toml               # Streamlit theme config
    ├── .env                          # Spotify credentials (not in git)
    ├── .gitignore                    # Excludes .env and venv
    └── requirements.txt              # Python dependencies

## 🎨 Pages Overview
#### 🌌 My Genre Galaxy
- Visualizes your top 12 genres as planets orbiting in space. 
- The size of each planet represents how frequently you listen to that genre. 
- Built with Plotly's interactive scatter plot, each genre is positioned in a beautiful spiral pattern with neon plasma colors.

#### 🎤 Top Artists
- A stunning 3D bar chart showing your 10 most-listened artists with their Spotify popularity scores. 
- The visualization uses matplotlib's 3D capabilities with a dark theme and tilted perspective for a modern, dynamic look.

#### 🎵 Top Tracks
- An interactive scatter plot comparing the popularity and duration of your top 15 tracks. 
- Hover to see artist information. 
- The color intensity represents each track's popularity on Spotify.

#### 🕓 Listening Habits
- A heatmap showing which days and times you listen to music the most. 
- Brighter colors = more listening activity 
- Perfect for discovering your musical prime hours and favorite listening days!

#### 🌈 Aura Visualizer
- A musical mood visualization plotting tracks by energy (Y-axis), danceability (X-axis), and emotional positivity/valence (color). 
- This page uses simulated data for demonstration, creating a personalized "musical aura" that reflects your vibe and energy.

## 🔐 Privacy & Security
1. Your `.env` file is never committed to Git (see .gitignore)
2. Credentials are loaded from environment variables only
3. The dashboard uses fallback/sample data if no credentials are provided
4. No personal data is stored locally

## 📊 Fallback Data
All pages include beautiful sample data that displays automatically if:

- No `.env` file is found
- Spotify API credentials are invalid
- API requests fail

This means you can explore the dashboard's features even without Spotify authentication!

## 🛠️ Tech Stack
- Streamlit — UI framework
- Spotipy — Spotify API Python client
- Plotly — Interactive visualizations
- Matplotlib & Seaborn — Static charts
- Pandas & NumPy — Data manipulation

## 📦 Dependencies
```
streamlit
spotipy
pandas
plotly
numpy
matplotlib
seaborn
python-dotenv
```
## 🎯 Future Ideas
- Add time-based trends (listening over weeks/months)
- Implement artist recommendation engine
- Export data as PNG/PDF reports
- Add playlist analysis
- Create mood-based playlists

## 📝 License
This project is open source and available for personal use.

## 💬 Feedback
Found a bug? Have a feature idea? Feel free to open an issue or submit a PR!

