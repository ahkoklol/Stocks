import streamlit as st
from streamlit_calendar import calendar

st.set_page_config(
    page_title="Economic Calendar",
    page_icon="📅",
    layout="wide"
)

st.title("Economic Calendar")

# Define event data
events = [
    {"title": "GDP Report", "start": "2025-02-15", "color": "blue"},
    {"title": "Inflation Data Release", "start": "2025-02-20", "color": "red"},
    {"title": "Fed Interest Rate Decision", "start": "2025-02-25", "color": "green"},
    {"title": "Jobs Report", "start": "2025-02-28"},
]

# Display the calendar widget
cal = calendar(
    key="calendar",
    options={
        "editable": False,
        "selectable": True,
        "initialView": "dayGridMonth",
        "events": events,
        "height": 650,  # Increase calendar height
        "aspectRatio": 2,  # Adjust width-to-height ratio
    },
)

st.write(cal)