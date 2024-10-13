"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBToTiz23KwPLoUOK0gWF2odY6I6O2dLPk")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)

print("What is the Name of the Chapter:")
name_Of_Chapter = input()

input_string = "give me the formula and definations of important things in the chapter" + name_Of_Chapter
 

response = chat_session.send_message(input_string)

print(response.text)