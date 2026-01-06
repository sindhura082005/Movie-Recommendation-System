# 🎬 Movie Recommendation System

[![Streamlit Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.com)

A content-based recommender using TF-IDF and cosine similarity, enhanced with OMDB API for rich movie details.

## Features
- **Personalized Recommendations**: Finds similar movies based on genres, plot, cast
- **Rich UI**: Displays posters and plot summaries
- **Scalable Design**: Cached similarity matrix for fast responses

## Tech Stack
- Python (Pandas, NLTK, Scikit-learn)
- Streamlit (Deployment)
- OMDB API (Movie metadata)

## How to Run
```bash
pip install -r requirements.txt
streamlit run app/app.py
```
## 📸 Application Preview

<div align="center">
  <img src="app/assets/app-screenshot-1.png" width="45%">
  <img src="app/assets/app-screenshot-2.png" width="45%">
  <img src="app/assets/app-screenshot-3.png" width="45%">
  <br>
  <em>Left: Main interface | Right: Recommendation results</em>
</div>

## Sample Output
![Demo](assets/demo.gif) 

 <!-- Add screenshot -->

## Future Work
- [ ] Add user ratings (Hybrid Filtering)
- [ ] Deploy on AWS
