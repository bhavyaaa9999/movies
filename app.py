
import streamlit as st

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# -------------------- Custom CSS --------------------
st.markdown("""
<style>

/* Main App Background */
.stApp {
    background-color: #5B2C6F;
}

/* Main Text */
html, body, [class*="css"], p, div, span, label {
    color: #FFD700 !important;
}

/* Title */
h1 {
    color: #FFD700 !important;
    text-align: center;
    font-size: 50px;
}

/* Subheaders */
h2, h3 {
    color: #FFD700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #4A235A;
}

section[data-testid="stSidebar"] * {
    color: #FFD700 !important;
}

/* Selectbox */
div[data-baseweb="select"] {
    color: black;
}

/* Buttons */
.stButton > button {
    background-color: #FFD700;
    color: #4A235A;
    border: none;
    border-radius: 10px;
    padding: 10px 25px;
    font-size: 18px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #F4D03F;
    color: #4A235A;
}

/* Success Message */
div[data-testid="stAlert"] {
    background-color: #6C3483;
    color: #FFD700;
}

/* Footer */
footer {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# -------------------- Movie Data --------------------
movies = {
    "Avatar": [
        "Titanic",
        "Interstellar",
        "Gravity",
        "The Martian",
        "Guardians of the Galaxy"
    ],
    "Inception": [
        "Tenet",
        "The Matrix",
        "Shutter Island",
        "Memento",
        "The Prestige"
    ],
    "Titanic": [
        "The Notebook",
        "Avatar",
        "A Walk to Remember",
        "Pearl Harbor",
        "Romeo + Juliet"
    ],
    "Avengers: Endgame": [
        "Infinity War",
        "Iron Man",
        "Thor: Ragnarok",
        "Captain America: Civil War",
        "Doctor Strange"
    ],
    "Harry Potter": [
        "Fantastic Beasts",
        "The Hobbit",
        "The Chronicles of Narnia",
        "Percy Jackson",
        "The Lord of the Rings"
    ]
}

# -------------------- Sidebar --------------------
st.sidebar.title("🎥 Movie Recommender")
st.sidebar.write("Choose a movie and get recommendations!")

genre = st.sidebar.selectbox(
    "Select Genre",
    ["Action", "Adventure", "Drama", "Fantasy", "Sci-Fi"]
)

# -------------------- Main Page --------------------
st.title("🎬 Movie Recommendation System")

st.write("Select your favorite movie below and click the button to see recommendations.")

selected_movie = st.selectbox(
    "Choose a Movie",
    list(movies.keys())
)

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Popcorn.jpg",
    width=250
)

if st.button("🎬 Recommend Movies"):
    st.success("Top Movie Recommendations")

    for i, movie in enumerate(movies[selected_movie], start=1):
        st.write(f"⭐ {i}. {movie}")

st.markdown("---")
st.markdown(
    "<center><h4>Made with ❤️ using Streamlit</h4></center>",
    unsafe_allow_html=True
)