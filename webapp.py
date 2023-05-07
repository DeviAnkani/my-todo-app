import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    function.write_todos(todos)


st.title("My Todo App")
st.subheader("this is my todo app")
st.write("the app is increase your productivity")

for index,todo in enumerate(todos):
    checkbok = st.checkbox(todo,key =todo)
    if checkbok:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",placeholder="Add the todo...",
              on_change = add_todo,key="new_todo")


#print("hello")
#st.session_state
