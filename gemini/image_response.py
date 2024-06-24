from dotenv import load_dotenv
import os
import google.generativeai as genai
from settings import *
import asyncio


load_dotenv()

GEMINI_API_KEY : str = os.getenv("GEMINI_API_KEY_IMAGE")


with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()


async def image_response(text:str, image_file_name:str) -> str:
  
  genai.configure(api_key=GEMINI_API_KEY)
  def upload_to_gemini(path, mime_type=None):

   file = genai.upload_file(path, mime_type=mime_type)
   print(f"Uploaded file '{file.display_name}' as: {file.uri}")
   return file
  
  os.chdir("image")

  files = [
  upload_to_gemini(image_file_name, mime_type="image/jpeg")]

  os.remove(image_file_name)
  os.chdir("..")
  
  if text == None:
   return "no caption"
  
  else:
   generation_config : dict = generation_configs_main
   safety_settings : list = safety_settings_main

   model = genai.GenerativeModel(
     model_name="gemini-1.5-flash",
     safety_settings=safety_settings,
     generation_config=generation_config,
     system_instruction=text_sys
  )
   chat_session = model.start_chat(
    history=[
    ]
  )
  
  if text == None:
        response = chat_session.send_message([files[0]], stream=True)
        response.resolve()
        return response.text
   
  else: 
    response = chat_session.send_message([text, files[0]], stream=True)
    response.resolve()
    return response.text

          
 