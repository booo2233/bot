import asyncio
import os
from dotenv import load_dotenv
import google.generativeai as genai
from settings import *
import httpx
import aiofiles
import json

print("1")

load_dotenv()
GEMINI_KEY : str = os.getenv("GEMINI_API_KEY")
DEEPGRAM   : str = os.getenv("VOICE_API_KEY")
#genai.configure(api_key=GEMINI_KEY)

print("1")
url : str =  "https://api.deepgram.com/v1/listen"
url_voice : str = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"
print("1")

with open("system.txt", "r", encoding="utf-8") as f:
 text_sys = f.read()
 print("1")

print("1")
async def voice(file_name):
    print("1")
    print(file_name)
    headers = {
        "Authorization": f"Token {DEEPGRAM}",
        "Content-Type": "audio/ogg"
    }
    
    # Save the current directory
    print("1")
    
        # Change to the "audio" directory
    os.chdir("audio")
    print("1")
    async with httpx.AsyncClient() as client:
            
            # Open the audio file
            async with aiofiles.open(file_name, "rb") as audio_file:
                # Read the file content
                audio_data = await audio_file.read()
            
                # Send the request
                response = await client.post(url, headers=headers, content=audio_data)
                os.chdir("..")
                
                data = response.text
                json_data = json.loads(data)

                text = json_data["results"]["channels"][0]["alternatives"][0]["transcript"]

                
                genai.configure(api_key=GEMINI_KEY)

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
                   voice_text =  response
                
                else:
                    return
        
                  
# Define the headers
                headers = {
                    "Authorization": f"Token {DEEPGRAM}",
                    "Content-Type": "application/json"
                   }

# Define the payload
                payload = {
                   "text": voice_text
                    }

# Make the POST request
                print("1")
                response = await client.post(url_voice, headers=headers, json=payload)

# Check if the request was successful
                if response.status_code == 200:
    # Save the response content to a file
                   print("1")
                   os.chdir("audio")
                   async with aiofiles.open(file_name, "wb") as f:
                     await f.write(response.content)
                     os.chdir("..")
                     print("1")
                     return file_name
                    
                else:
                   print(f"Error: {response.status_code} - {response.text}")





  
#key
  
