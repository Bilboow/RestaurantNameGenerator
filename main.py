import streamlit as st
import helper

st.title("Restaurant Name Generator")
#"Indian", "Italian", "Mexican", "Arabic", "American"
cuisine = st.sidebar.selectbox("Pick up a curisine",("Indian", "Italian", "Mexican", "Arabic", "American", "Chinese"))

if cuisine:
    response = helper.generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response['menu_items'].strip().split(",")
    st.write("****Menu Items****")
    for item in menu_items:
        st.write("-",item)

