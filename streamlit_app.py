import streamlit as st


with st.sidebar:
    number_of_elements = st.selectbox('Number of elements', 
                              ('2','3','4'), 
                              index=None, 
                              placeholder='3')

st.title("🎈 Disorder in crystals")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)