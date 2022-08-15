import streamlit as st

st.sidebar.image("https://cdn.britannica.com/97/1597-004-05816F4E/Flag-India.jpg")

Name = st.sidebar.text_input("Enter Your Name")

st.sidebar.image("https://img.freepik.com/free-vector/15th-august-happy-independence-day-india_1017-20000.jpg?w=2000")
name = Name.capitalize()
img = st.image("https://cbpacs.com/wp-content/uploads/2022/08/Independence-Day-2022-Status.jpg"
         ,caption=f"Dear {name}, May we enjoy the freedom of thoughts, freedom of speech, and freedom of choice for the rest of our lives. Happy Independence Day!")
