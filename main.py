import streamlit as st
from functions import *


todos = read_todos()


def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo + '\n')
    write_todos(todos)



title = '<h1 style="font-family:Helvetica; color:Blue; size:20">To Do List</h1>'
date = get_date()
date_display = f'<h2 style="font-family:Helvetica; color:Green: size:10">{date}</h2>'
st.markdown(date_display, unsafe_allow_html=True)
st.markdown(title, unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=index)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[index]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")








