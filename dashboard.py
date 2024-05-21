import streamlit as st

st.set_page_config(page_title="resturaunt access dashboard" , page_icon=":tada", layout="wide")

# ---- HEADER SECTION ----
with st.container():
    st.title("please choose the task you want to do from the side menu.")
    st.sidebar.success("Select a page.")
