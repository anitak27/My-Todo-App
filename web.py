import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    todos.append(new_todo + '\n')
    f.save_todos(todos)
    st.session_state['new_todo'] = ''


st.title('My Todo App')
st.subheader('An easy way to manage productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.save_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')
