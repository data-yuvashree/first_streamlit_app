import streamlit
import pandas

streamlit.title("My Parent's New Healthy Diner")

streamlit.header("Menu For the Day")
streamlit.text("Omega 3 and Blueberry Oatmeal")
streamlit.text("Kale and Spinach Smoothie")
streamlit.text("Hard Boiled Egg")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
