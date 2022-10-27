import streamlit as st
from spell import correction

st.title("hello")
check = st.sidebar.checkbox('Show the original input word')
form = st.form(key='form-name')
selected_word = form.selectbox('Select a word:', ['', 'valubale', 'levels', 'choise', 'extreamly'])
input_word = form.text_input('OR Type your own word!')

submit = form.form_submit_button("Submit")


if check:
    if selected_word != '':
        st.write("Original input word:", selected_word)
    elif input_word != '':
        st.write("Original input word:", input_word)

if submit:
    word = ""
    if (selected_word != ''):
        word = selected_word
    elif (input_word != ''):
        word = input_word

    correct = correction(word)
    if (word == correct):
        st.success(f"{word} is the correct spelling!")
    else:
        st.error(f"Correction: {correct}")
    # st.title(a)
