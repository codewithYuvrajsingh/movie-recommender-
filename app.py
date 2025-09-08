import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st

# Load the data
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Create a user-movie matrix
user_movie_matrix = ratings.pivot_table(index="userId", columns="movieId", values="rating").fillna(0)

# Compute cosine similarity between movies
movies_similarity = cosine_similarity(user_movie_matrix.T)
movies_similarity_df = pd.DataFrame(
    movies_similarity, 
    index=user_movie_matrix.columns,
    columns=user_movie_matrix.columns
)

def recommend(movie_title, top_n=5):
    # Find movie ID
    movie_id = movies[movies['title'].str.lower() == movie_title.lower()]["movieId"].values
    if len(movie_id) == 0:
        return []
    movie_id = movie_id[0]

    # Get similarity scores
    sim_scores = movies_similarity_df[movie_id].sort_values(ascending=False)

    # Pick top_n similar movies (excluding the movie itself)
    top_movies_ids = sim_scores.iloc[1:top_n+1].index
    top_movies = movies[movies["movieId"].isin(top_movies_ids)]["title"].tolist()

    return top_movies

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie:", movie_list)

if st.button("Get Recommendations"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.subheader(f"✨ Top Recommendations for '{selected_movie}':")
        for i, rec in enumerate(recommendations, start=1):
            st.write(f"{i}. {rec}")
    else:
        st.warning("Movie not found in the dataset.")
