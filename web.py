import streamlit as st
import function

todos = function.get_todos()
st.title("My Todo Web App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo",placeholder="Add new todo ...")
print ("helo")