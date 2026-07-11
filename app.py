import streamlit as st


st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)


st.markdown("""
<style>

.stApp{
    background-color:#EAF4FC;
}

h1{
    color:#0B5394;
    text-align:center;
}

.stButton>button{
    background-color:#0B5394;
    color:white;
    border-radius:10px;
    height:45px;
    width:170px;
    font-size:18px;
}

.stButton>button:hover{
    background-color:#1C75BC;
    color:white;
}

</style>
""", unsafe_allow_html=True)


movies = {
    "Avatar": [
        "Titanic",
        "Interstellar",
        "Gravity",
        "The Martian",
        "Guardians of the Galaxy"
    ],

    "Inception":[
        "Tenet",
        "The Matrix",
        "Shutter Island",
        "Memento",
        "The Prestige"
    ],

    "Titanic":[
        "The Notebook",
        "Avatar",
        "A Walk to Remember",
        "Pearl Harbor",
        "Romeo + Juliet"
    ],

    "Avengers: Endgame":[
        "Infinity War",
        "Iron Man",
        "Thor Ragnarok",
        "Captain America",
        "Doctor Strange"
    ],

    "Harry Potter":[
        "Fantastic Beasts",
        "The Hobbit",
        "The Chronicles of Narnia",
        "Percy Jackson",
        "Lord of the Rings"
    ]
}


st.sidebar.title("🎥 Movie Recommender")

st.sidebar.info(
"""
This is a simple Movie Recommendation System built using Streamlit.

Choose a movie and click the Recommend button.
"""
)

genre = st.sidebar.selectbox(
    "Select Genre",
    [
        "Action",
        "Adventure",
        "Sci-Fi",
        "Fantasy",
        "Drama"
    ]
)


st.title("🎬 Movie Recommendation System")

st.write(
"""
Welcome!

Select your favourite movie and discover similar movies.
"""
)


selected_movie = st.selectbox(
    "Choose a Movie",
    list(movies.keys())
)


st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Popcorn.jpg",
    width=250
)


if st.button("🎬 Recommend Movies"):

    st.success("Top Recommendations")

    recommendations = movies[selected_movie]

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. ⭐ {movie}")


st.markdown("---")
st.caption("Made with ❤️ using Streamlit")