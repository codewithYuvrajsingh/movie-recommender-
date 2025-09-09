
🎬 Movie Recommender System

A simple Movie Recommender System built with Python, Pandas, and Streamlit.
This app recommends movies to users based on their past ratings using cosine similarity.

🚀 Features

📂 Loads movie and rating datasets (CSV files).

🧮 Builds a user-movie rating matrix.

🔍 Uses cosine similarity to compute movie-to-movie closeness.

🎥 Recommends movies similar to the one selected by the user.

🌐 Interactive Streamlit UI for easy exploration.

🛠 Tech Stack

Python 3.x

Pandas – data manipulation

Scikit-learn – cosine similarity

Streamlit – web interface

📦 Installation

Clone the repository:

git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux


Install dependencies:

pip install -r requirements.txt

▶️ Usage

Run the Streamlit app:

streamlit run app.py


Then open the app in your browser at http://localhost:8501
.

📂 Project Structure
movie-recommender/
│-- app.py                # Main Streamlit app
│-- movies.csv            # Movies dataset
│-- ratings.csv           # Ratings dataset
│-- requirements.txt      # Project dependencies
│-- README.md             # Documentation

🔮 Future Improvements

Add content-based filtering (genres, tags).

Add collaborative filtering (user-based recommendations)

Improve UI with posters & more details.
