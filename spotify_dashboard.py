import streamlit as st

st.set_page_config(page_title="My Spotify Dashboard", page_icon="🎧", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
.stApp {
    background-image: url("https://i.pinimg.com/736x/11/8a/38/118a38bec53b81b640960f71ee6237b0.jpg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}
.centered {
    background-color: rgba(0,0,0,0.6);
    padding: 3em;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-top: 10vh; /* add space above to center vertically */
}
</style>
""", unsafe_allow_html=True)
st.markdown('<div class="centered"><h1>🎧 manpreet\'s spotify insights</h1>'
            '<p>welcome to a data-driven look into my Spotify world — '
            'where music meets data and visuals. ' 
            'dive in to explore my top tracks, artists, and more...</p>'
            '</div>', unsafe_allow_html=True)

st.write("")

st.button("→ To access details of the project, click the links on top left.")








