import streamlit as st
from PIL import Image

st.set_page_config(page_title="resturaunt access dashboard" , page_icon=":tada", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("RESTAURANT DATABASE ACCESS DASHBOARD")
    st.subheader("please choose the task you want to do from the side menu.")
    st.sidebar.success("Select a page.")

    # Load and display the image
image = Image.open("Schema.jpg")

st.image(image, caption="Schema Diagram", use_column_width=True)
