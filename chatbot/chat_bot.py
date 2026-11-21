from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# using openai wrapper to call groq api
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
    )

def bot(query):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": query}
        ]
    )
    # response.choices - > list of choices(LLM may reply with multiple choices), each choice has a message with content
    return response.choices[0].message.content

def main():
    user_input = input("You: ")
    print(bot(user_input))

if __name__ == '__main__':
    main()