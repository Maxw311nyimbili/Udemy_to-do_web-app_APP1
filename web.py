import streamlit as st
import functions

# getting the to-do items from the file todos.txt as
# a list in a variable todos
todos = functions.get_todos()


# session_state has the structure of a dictionary. And in the function below, it is connected to the
# st.text_input() through the on_change. session_state adopts the key given to under st.text_input.
# the value of this key will be what the user inputs the input space.
def add_todo():
    activity = st.session_state["new_todo"] + "\n"  # getting value using key "new_todo"
    todos.append(activity)

    if st.session_state["new_todo"] + "\n" == "" + "\n":
        print("Hello")
    else:
        functions.write_todos("todos.txt", todos)  # original list is updated to the new instance of the list that
    # has an appended activity to it


# Heading of the app
st.title("My Todo App")

# displaying to-do items on the app
# by iterating through the todos list
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos("todos.txt", todos)  # original list is updated to the new instance of the list that
        # has an appended activity to it
        del st.session_state[todo]  # removes the checked to-do from the session_state "dictionary"
        st.experimental_rerun()


st.text_input(label="To-do", placeholder="Enter to-do activity", on_change=add_todo, key="new_todo")


