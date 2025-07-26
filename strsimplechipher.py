import streamlit as st

def shift_letters(word):
    shifted = ""
    for char in word:
        if char.isalpha():
            if char.islower():
                shifted += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                shifted += chr((ord(char) - ord('A') + 1) % 26 + ord('A'))
        else:
            shifted += char
    return shifted

st.title("🔐 Letter Shifter by 1 Position")

user_input = st.text_input("Enter a word:")

if user_input:
    result = shift_letters(user_input)
    st.success(f"🔁 Shifted Word: **{result}**")
