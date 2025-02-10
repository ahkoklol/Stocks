import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(
    page_title = "Name to be chosen",
    page_icon = "📈",
)

st.title("Economic Calendar")



calendar = calendar(
    key='calendar', # Assign a widget key to prevent state loss
    )
st.write(calendar)