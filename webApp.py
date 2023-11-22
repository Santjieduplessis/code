# when deploying: terminal -> pip freeze > requirements.txt
import streamlit as st
import functions as f

def add_item():
    new_item = st.session_state["new_item"]
    myList.append(new_item + '\n')
    f.file_function(filepath, 'w', myList)
    st.session_state["new_item"] = ""

filepath = 'todos.txt'
myList = f.file_function(filepath, 'r', "")


st.title("My Web App")
st.subheader("This is a subheader")
st.write("List of grocery")

for index, item in enumerate(myList):
    checked = st.checkbox(item, key=item)
    if checked:
        myList.pop(index)
        f.file_function(filepath, 'w', myList)
        del st.session_state[item]
        st.rerun()

st.text_input(label="input", label_visibility="hidden", placeholder="Enter a new fruit", on_change=add_item, key="new_item")