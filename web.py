import streamlit as st
import function



todos = function.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    # print(todo)
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo Web App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")


for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a todo",placeholder="Add new todo ...",
              on_change=add_todo,key="new_todo")

st.session_state
# print ("helo")