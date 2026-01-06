# 🎥Movie-Recommendation-System

A content-based recommender using TF-IDF and cosine similarity, enhanced with OMDB API for rich movie details.


# ✨ Features
---
  Personalized Recommendations: Finds similar movies based on genres, plot, cast

  Rich UI: Displays posters and plot summaries

  Scalable Design: Cached similarity matrix for fast responses

  Real-time movie posters & plots using OMDB API

  # 🧪 Tech Stack
  ---
  
  |Frontend|Backend|ML/Tools|
|--------|-------|--------|
|Streamlit|OMDB API (REST)|Cosine Similarity|
|HTML/CSS (auto)|Python + Requests|Scikit-learn|
|Vercel|API Key Injection|Pandas, NumPy|


## 📁 Project Structure
---
movie-recommendation-system-main/
│
├── app/
│   ├── app.py                 # Streamlit application logic
│   └── assets/                # App screenshots & static assets
│       ├── app-screenshot-1.png
│       ├── app-screenshot-2.png
│       └── app-screenshot-3.png
│
├── data/
│   └── movies.csv             # Movie metadata dataset
│
├── .env                       # Environment variables (API keys)
├── .gitignore                 # Git ignored files
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation



