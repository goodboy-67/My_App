import streamlit as st
from openai import OpenAI
from st_chat_message import message

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


system_prompt = 'You are a good chatgpt who is nice to people who ask questions.'

if 'convo' not in st.session_state:
    st.session_state['convo'] = {"role":'system',"content":system_prompt}

for chat in st.session_state['convo']:
    if chat['role'] == 'system':
        continue
    elif chat['role']=='user':
        message(chat['content'],is_user=True)
    else:
        message(chat['content'])


with st.form('input'):

    user_input = st.text_input("This is the start of your legendary conversation with chatgpt500")
    submitted = st.form_submit_button('Send Message')

    if submitted and user_input != "":
        st.session_state['convo'].append({'role':'user','content':user_input})


chat = [
    {'role':'system','content':system_prompt},
    {'role':'user','content':user_input}
]

response = get_standard_response(chat)

st.write(response)