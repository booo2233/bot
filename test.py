"""
from PIL import Image
import os
from settings import *
import google.generativeai as genai
from dotenv import load_dotenv
import asyncio
load_dotenv()

key : str = os.getenv("GEMINI_API_KEY")

async def handle_response_image(text: str) -> str:
 genai.configure(api_key=key)


# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
 generation_config : dict = generation_configes
 safety_settings : list = safety_settingses


 model = genai.GenerativeModel(
   model_name = "gemini-1.5-pro",
   safety_settings = safety_settings,
   generation_config = generation_config,
 )

 img = Image.open('')
 img

 response = model.generate_content([text, img], stream=True)
 response.resolve()
 
 return response.text

print(handle_response_image("what is in image"))
"""
"""
def num(number):
    len_num = len(number) -1
    hr = True

    while hr:
        hr = False
        for i in range(0, len_num):
            if number[i] > number[i + 1]:
                number[len_num], number[i + 1] = number[i + 1], number[i]  
                hr = True
    return number
print(num([2,4,5,6,34,5,6,3,5,4,42,56,3,455,5,5,45,533]))
"""
    
num = [2,4,5,6,34,5,6,3,5,4,42,56,3,455,5,5,45,533]

num = num[-5:-1]

print(num)


  
    
        


    
