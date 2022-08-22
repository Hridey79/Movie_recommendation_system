from requests import request
import streamlit as st
import pickle

movies=pickle.load(open("./EDA/df.pkl",'rb'))
movie_list=movies['title'].values
sim_mat=pickle.load(open("./EDA/sim_mat.pkl",'rb'))
import requests

def fetch_poster(movie_id):
    response=requests.get(
        "https://api.themoviedb.org/3/movie/{}?api_key=2faf42cc6955b829d89b8e3bffd8b844&language=en-US".format(movie_id)
        )
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path'], data['overview']
    

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(sim_mat[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_summary = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        poster,summary=fetch_poster(movie_id)
        recommended_movie_posters.append(poster)
        recommended_movie_summary.append(summary)
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters,recommended_movie_summary

st.title("Movie Recommendation System")

selected_movie_name= st.selectbox("Type or select a movie from the dropdown",movie_list)
if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_summary = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        with st.expander("Summary"):
            st.text_area(recommended_movie_summary[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        with st.expander("Summary"):
            st.text_area(recommended_movie_summary[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        with st.expander("Summary"):
            st.text_area(recommended_movie_summary[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        with st.expander("Summary"):
            st.text_area(recommended_movie_summary[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        with st.expander("Summary"):
            st.text_area(recommended_movie_summary[4])


