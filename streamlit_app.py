import streamlit
streamlit.title("My Mom's new healthy diner")
streamlit.header(' Breakfast favourates')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 avagadro Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
