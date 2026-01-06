import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
import re
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests
import os
from pathlib import Path
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

parent_dir = Path(__file__).parent.parent
env_path = parent_dir / ".env"

if env_path.exists():
    load_dotenv(dotenv_path=env_path)
else:
    st.error(".env file not found in parent directory!")
    st.stop()

API_KEY = os.getenv("OMDB_KEY")
if not API_KEY:
    st.error("OMDB API key missing in .env file!")
    st.stop()

nltk.download("stopwords", quiet=True)
stop_words = set(stopwords.words("english"))

st.set_page_config(page_title="Movie Recommendation System", layout="centered")
st.title("🎬 Movie Recommendation System")
st.write("Type a movie name to get similar recommendations")

PLACEHOLDER_POSTER = "https://via.placeholder.com/200x300?text=No+Poster"

def safe_show_image(url, width=200):
    try:
        if not url:
            raise ValueError("Invalid image URL")

        response = requests.get(url, timeout=5)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        st.image(image, width=width)

    except Exception:
        st.image(PLACEHOLDER_POSTER, width=width)

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies.csv")
    data = df[["title", "genres", "keywords", "overview", "cast", "director"]]
    data = data.dropna()
    data["combined"] = (
        data["genres"]
        + " "
        + data["keywords"]
        + " "
        + data["overview"]
        + " "
        + data["cast"]
        + " "
        + data["director"]
    )
    return data

@st.cache_data
def preprocess_data(data):
    def clean_text(text):
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
        text = text.lower()
        words = [w for w in text.split() if w not in stop_words]
        return " ".join(words)

    data["cleaned"] = data["combined"].apply(clean_text)
    return data

@st.cache_resource
def create_similarity_matrix(data):
    tfidf = TfidfVectorizer(max_features=5000)
    matrix = tfidf.fit_transform(data["cleaned"])
    return cosine_similarity(matrix, matrix)

def recommended_movies(movie_name, data, similarity, n=5):
    matches = data[data['title'].str.lower().str.contains(movie_name.lower())]

    if matches.empty:
        return None

    ind = matches.index[0]  
    scores = list(enumerate(similarity[ind]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:n+1]

    movie_indices = [i[0] for i in scores]
    return data['title'].iloc[movie_indices]


def get_movie_details(title):
    url = f"http://www.omdbapi.com/?apikey={API_KEY}&t={title}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        res = response.json()

        if res.get("Response") == "True":
            plot = res.get("Plot", "Plot not available")
            poster = res.get("Poster")

            if poster in (None, "N/A", ""):
                poster = None

            return plot, poster
    except Exception:
        pass

    return "Plot not available", None

with st.spinner("Loading movie database..."):
    data = load_data()
    data = preprocess_data(data)
    cosine_sim = create_similarity_matrix(data)

movie_name = st.text_input("Enter a movie name:", "The Dark Knight Rises")
num_recommendations = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Get Recommendations"):
    with st.spinner("Finding similar movies..."):
        recommendations = recommended_movies(
            movie_name, data, cosine_sim, num_recommendations
        )

        if recommendations is None:
            st.error("Movie not found in database. Please check spelling.")
        else:
            st.success(f"🎥 Movies similar to '{movie_name}':")

            plot, poster = get_movie_details(movie_name)
            st.subheader(f"About '{movie_name}':")

            col1, col2 = st.columns([1, 2])
            with col1:
                safe_show_image(poster, width=200)
            with col2:
                st.write(plot)

            st.markdown("---")

            
            st.subheader("Recommended Movies")

            for i, movie in enumerate(recommendations, 1):
                plot, poster = get_movie_details(movie)
                cols = st.columns([1, 3])

                with cols[0]:
                    safe_show_image(poster, width=150)

                with cols[1]:
                    st.markdown(f"**{i}. {movie}**")
                    st.caption(plot)

                st.markdown("---")

st.markdown(
    """
<style>
.stTextInput>div>div>input {
    font-size: 18px;
    padding: 12px;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    padding: 12px 24px;
    border-radius: 4px;
    font-size: 16px;
}
</style>
""",
    unsafe_allow_html=True,
)
