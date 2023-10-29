import streamlit as st
from utils import prompt_to_json

def main():
    st.title("LLM interface for SubZero's Infinite Dataset")

    user_input = st.text_area("Enter prompt:")
    result = None

    if st.button("Enter"):
        result = prompt_to_json(user_input)

    if result:
        st.sidebar.subheader("Dictionary:")
        st.sidebar.json(result)

if __name__ == "__main__":
    main()

# "The weather is sunny and there is very heavy traffic. There are 2 dogs nearby and a few potholes."