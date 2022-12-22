import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select the data to view", ("Temperature", "Sky conditions"))
days_word = "days" if int(days) > 1 else "day"

if place:
    try:
        data = get_data(place, days)
        st.subheader(f"{option} for the next {days} {days_word} in {place}")

        if option == "Temperature":
            # temperature plot
            dates = [item["dt_txt"] for item in data]
            temperatures = [item["main"]["temp"] for item in data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (F)"})
            st.plotly_chart(figure)

        if option == "Sky conditions":
            # sky conditions chart
            sky_conditions = [item["weather"][0]["main"] for item in data]
            image_list = [f"images/{str(condition).lower()}.png" for condition in sky_conditions]

            st.image(image_list, width=115)

    except KeyError:
        st.subheader(f"Could not find a location named {place}")
