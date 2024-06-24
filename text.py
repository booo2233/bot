"""
import google.generativeai as genai
import os
import time
from settings import *
import asyncio

print("lol")
key = "AIzaSyDhpGqvdZVhWE73HW_z_CKCcbYMVa6SAqo"
genai.configure(api_key=key)

def upload_to_gemini(path, mime_type=None):
  
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  print("lol")
  return file
  
  
print("lol")


files = [
upload_to_gemini("r.mp3", mime_type="audio/mp3"),
 ]
print("lol")
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    safety_settings=safety_settingses,
    generation_config=generation_configes,
    system_instruction="be good ai your name = gemini"
                              )
print("lol")
# Make the LLM request.
print("Making LLM inference request...")
print(files)
response = model.generate_content([files[0]])
print(response.text)
print("""
"""
import requests

# Define the API endpoint
url = "https://api.deepgram.com/v1/speak?model=aura-asteria-en"

# Set your Deepgram API key
api_key = "DEEPGRAM_API_KEY"

# Define the headers
headers = {
    "Authorization": f"Token {"955a435ca5d640c7ea10afcd88f0d4b137d3d29a"}",
    "Content-Type": "application/json"
}

# Define the payload
payload = {
    "text": "Hello, how can I help you today?"
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    # Save the response content to a file
    with open("your_output_file.mp3", "wb") as f:
        f.write(response.content)
    print("File saved successfully.")
else:
    print(f"Error: {response.status_code} - {response.text}")

"""
"""
import requests
import pprint
# Define the URL for the Deepgram API endpoint
url = "https://api.deepgram.com/v1/listen"

# Define the headers for the HTTP request
headers = {
    "Authorization": f"Token {"955a435ca5d640c7ea10afcd88f0d4b137d3d29a"}",
    "Content-Type": "audio/mp3"
}

# Get the audio file
with open("your_output_file.mp3", "rb") as audio_file:
    # Make the HTTP request
    response = requests.post(url, headers=headers, data=audio_file)

print(response.json())
"""
import json

# Example JSON data
json_data = '''
{
    "metadata": {
        "transaction_key": "deprecated",
        "request_id": "f8b96f56-9f65-4b5b-b0a6-de2e7b852a61",
        "sha256": "77c7278a1b763a0f2b8e7c41bb505040327688fb8d240d67fda991a449243ee7",
        "created": "2024-06-18T18:59:00.235Z",
        "duration": 2.0375626,
        "channels": 1,
        "models": ["1ed36bac-f71c-4f3f-a31f-02fd6525c489"],
        "model_info": {
            "1ed36bac-f71c-4f3f-a31f-02fd6525c489": {
                "name": "general",
                "version": "2024-01-26.8851",
                "arch": "base"
            }
        }
    },
    "results": {
        "channels": [
            {
                "alternatives": [
                    {
                        "transcript": "hello how can i help you today",
                        "confidence": 0.99609375,
                        "words": [
                            {"word": "hello", "start": 0.1951923, "end": 0.42942306, "confidence": 0.9980469},
                            {"word": "how", "start": 0.5855769, "end": 0.74173075, "confidence": 0.9916992},
                            {"word": "can", "start": 0.74173075, "end": 0.81980765, "confidence": 0.9975586},
                            {"word": "i", "start": 0.9759615, "end": 1.1321154, "confidence": 0.9975586},
                            {"word": "help", "start": 1.1321154, "end": 1.2882692, "confidence": 0.99853516},
                            {"word": "you", "start": 1.2882692, "end": 1.6005769, "confidence": 0.99121094},
                            {"word": "today", "start": 1.6005769, "end": 1.7567307, "confidence": 0.99609375}
                        ]
                    }
                ]
            }
        ]
    }
}
'''

# Parse JSON data
data = json.loads(json_data)

# Extract the transcript safely with error handling
try:
    transcript = data["results"]["channels"][0]["alternatives"][0]["transcript"]
    print(transcript)
except (KeyError, IndexError) as e:
    print(f"Error extracting transcript: {e}")
