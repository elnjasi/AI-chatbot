import os
import openai
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv(dotenv_path="Key.env")

# Set OpenAI API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

def restaurant_chatbot(prompt, model="gpt-3.5-turbo"):
    system_message = "You are a helpful assistant that provides information about universities."
    user_message = {"role": "user", "content": prompt}
    messages = [{"role": "system", "content": system_message}, user_message]

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=150
    )

    ai_reply = response.choices[0].message["content"]
    return ai_reply

user_prompt = "Tell me about the best univeristy in new york."
chatbot_response = restaurant_chatbot(user_prompt)

print(chatbot_response)
