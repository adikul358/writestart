import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

"""
def chat(inp, message_history, role="user"):
    message_history=[]
    message_history.append({"role": role, "content": f"{inp}"})
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=message_history
    )
    reply_content = completion.choices[0].message.content
    #message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return reply_content
"""

def chat(inp, message_history=[], role="user"):
    message_history.append({"role": role, "content": f"{inp}"})
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=message_history
    )
    print(message_history)
    reply_content = completion.choices[0].message.content
    return reply_content
