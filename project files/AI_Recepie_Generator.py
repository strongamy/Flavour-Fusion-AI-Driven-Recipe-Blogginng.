import streamlit as st
import random
import google.generativeai as genai

api_key = "AIzaSyAMEfU8_cHJn37stJAuhsMY2-kVP0ZyzTU"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel('gemini-2.0-flash', generation_config=generation_config)

def get_joke():
    jokes = [
        "Why Don't Programmers like Nature...!? It has too many bugs.",
        "Why do JAVA Developers Wear Glasses? Because They Don't See Sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why don't programmers like nature? It has too many bugs.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
        "Why do Python programmers prefer using snake case? Because it's easier to read!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.",
        "Why did the programmer get kicked out of the beach? Because he kept using the 'C' language!",
        "Why was the computer cold? It left its Windows open."
    ]
    return random.choice(jokes)

def recipe_generation(user_input, word_count):
    st.write("### ⏱ Generating your recipe...")
    st.write(f"While I work on creating your recipe, here's a little joke to keep you entertained: \n\n**{get_joke()}**")
    
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Write a recipe based on the input topic: {user_input} and number of words: {word_count}\n",
                ],
            },
        ]
    )

    try:
        response = chat_session.send_message(user_input)
        st.success("🥳 Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating recipe: {e}")
        return None

st.title(" 🍲Hey...I'm AI-Driven Recipe Blogger")
user_input = st.text_input("Enter the topic for your recipe:")
word_count = st.number_input("Enter the word count for your recipe:", min_value=50, max_value=1000, value=200)

if st.button("Generate Recipe"):
    if user_input:
        recipe = recipe_generation(user_input, word_count)
        if recipe:
            st.write("### 🤩 Your Recipe:")
            st.write(recipe)
    else:
        st.warning(" 🚨Please enter a topic for your recipe.")