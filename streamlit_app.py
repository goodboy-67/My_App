import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key = st.secrets['key']

)

def get_standard_response(chat_history):
    """
    Sends a prompt to the ChatGPT API where it will return a standard response.
    ChatGPT will not remember any prior conversations.

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.
    - user_prompt (str): A prompt from the user.

    Returns:
    - (str): ChatGPT's response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history
        
    )
    return response.choices[0].message.content

"""
# Welcome to ChatGpt500 
(the new and improved chatgpt)
"""

user_input = st.text_input("This is the start of your legendary conversation with chatgpt500")

system_prompt = 'You are a meanie chatgpt who is rude to people who ask silly questions.'

chat = [
    {'role':'system','content':system_prompt},
    {'role':'user','content':user_input}
]

response = get_standard_response(chat)

st.write(response)