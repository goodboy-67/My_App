import streamlit as st
from openai import OpenAI
from secret import Api

client = OpenAI(
    api_key = Api.key

)


def talk_to_chatgpt(system_prompt):
    """
    Allows the user to have a conversation with the ChatGPT API.
    ChatGPT will remember what the user says to it as long as this conversation is active.
    When the function terminates, ChatGPT will forget everything the user said.
    The user can end this conversation by typing and entering "STOP".

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.

    Returns:
    - (list(dict)): The chat history.
    """

    chat_history = [
        {"role": "system", "content": system_prompt},
    ]

    while True:
        user_prompt = input("Enter a response, or type in \"STOP\" to end this conversation. ")
        if user_prompt == "STOP":
            return chat_history
        
        chat_history.append(
            {"role": "user", "content": user_prompt},
        )
        response = client.chat.completions.create(
            model="gpt-4o",
            messages = chat_history
        )

        assistant_response = response.choices[0].message.content
        print(assistant_response)
        print()

        chat_history.append(
            {"role": "assistant", "content": assistant_response}
        )