import numpy as np
import pandas as pd
import streamlit as st

from cards import (
    auth_card,
    charts_card,
    chat_card,
    dataframe_card,
    layouts_card,
    media_card,
    status_card,
    text_card,
    widgets_card,
)
from utils.umami import load_umami

load_umami()
if "init" not in st.session_state:
    st.session_state.chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.session_state.map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=["lat", "lon"],
    )
    st.session_state.init = True


st.logo(
    "static/streamlit.png",
    icon_image="static/datatreehouse.circle.png",
    size="large",
    link="https://datatreehouse.org",
)

pages = [
    st.Page("home.py", title="Home", icon=":material/home:"),
    st.Page("widgets.py", title="Widgets", icon=":material/widgets:"),
    st.Page("text.py", title="Text", icon=":material/article:"),
    st.Page("data.py", title="Data", icon=":material/table:"),
    st.Page("charts.py", title="Charts", icon=":material/insert_chart:"),
    st.Page("media.py", title="Media", icon=":material/image:"),
    st.Page("layouts.py", title="Layouts", icon=":material/dashboard:"),
    st.Page("chat.py", title="Chat", icon=":material/chat:"),
    st.Page("status.py", title="Status", icon=":material/error:"),
    st.Page("auth.py", title="Auth", icon=":material/lock:"),
]


page = st.navigation(pages)
page.run()

with st.sidebar.container(height=310):
    if page.title == "Widgets":
        widgets_card()
    elif page.title == "Text":
        text_card()
    elif page.title == "Data":
        dataframe_card()
    elif page.title == "Charts":
        charts_card()
    elif page.title == "Media":
        media_card()
    elif page.title == "Layouts":
        layouts_card()
    elif page.title == "Chat":
        chat_card()
    elif page.title == "Status":
        status_card()
    elif page.title == "Auth":
        auth_card()
    else:
        st.page_link("home.py", label="Home", icon=":material/home:")
        st.write("Welcome to the home page!")
        st.write(
            "Select a page from above. This sidebar thumbnail shows a subset of "
            "elements from each page so you can see the sidebar theme."
        )

st.sidebar.caption("This app uses [Poppins](https://fonts.google.com/specimen/Poppins) font.")
st.sidebar.markdown("[![buy-us-a-coffee](./app/static/buy-us-a-coffee.png)](https://pos.snapscan.io/qr/Ew6rBAsV)")
