
import httpx
from dotenv import load_dotenv
import os
import google.generativeai as genai
from settings import *
import asyncio

text_sys : str = ""
load_dotenv()
key = os.getenv("GEMINI_API_KEY")

image_name : str = ""
print(image_name)

with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()



async def handle_response(text: str,) -> str:
#key
  genai.configure(api_key=key)

  generation_config : dict = generation_configs_main
  safety_settings : list = safety_settings_main

  model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
    system_instruction=text_sys
  )
  chat_session = model.start_chat(
    history=[
    ]
  )
#main sand api call
  if text != None:
     text = text.lower()
  
     response = chat_session.send_message(text)
     response = response.text
     response = response.replace("*", "")
     return response
  else:
           response = chat_session.send_message(text, stream=True)
           print(response)
           response = response.text
           response = response.replace("*", "")
           return response

       

