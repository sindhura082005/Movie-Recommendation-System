# 🎥Movie-Recommendation-System

http://localhost:8501/

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


# 📁 Project Structure
---

```text
movie-recommendation-system-main/
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
└── LICENSE                    # MIT License
```

# 📦 Installation & Setup
---
    Install Requirements --> pip install -r requirements.txt

    Run the App Locally --> streamlit run app.py


# 📸 Application Preview
---
<img width="1462" height="929" alt="image" src="https://github.com/user-attachments/assets/62247729-2037-4ebf-8107-5660030225ef" />

<img width="1559" height="923" alt="image" src="https://github.com/user-attachments/assets/9dd3d3fd-a0eb-491f-b77f-1a4c0a190744" />

<img width="1443" height="944" alt="image" src="https://github.com/user-attachments/assets/9b3870d2-7c09-4a83-afb0-060aefdf2f6f" />



# 🔮 Future Improvements
---
   Add fuzzy matching for movie names

   Support hybrid (content + collaborative) filtering

   Deploy on Streamlit Cloud

   Add user ratings & feedback loop
