import streamlit as st

def app():
    st.title("Instructions")

    st.header("Navigating our web application")

    st.markdown(
    """
    To navigate our web application, the sidebar (left of the screen) can be used. Here, we list the available pages:
    - **About Us**: Contextualizing the web application, authors who worked on this project and credits for the resources used.
    - **Instructions**: Explaining how the web application is divided, and how this tool.
    - **User GUI**: Contains two tools for using the model. The first can be used for generating random images using our retrained model. The second must be enabled using the first, but can be used to generate animations containing the transition between two images.
    """)

    st.header("Using our image generation tool")
    st.video('https://youtu.be/rtU-PI-Lbxo')

    st.header("Using our image transition tool")
    st.video('https://youtu.be/KQ0taZxkPKk')