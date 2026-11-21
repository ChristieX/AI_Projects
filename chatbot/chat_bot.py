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


class ChatBot:
    def __init__(self):
        self.messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
        self.total_tokens = 0

    def bot(self, query):
        self.messages.append({"role": "user", "content": query})
        # LLM parameters:
            # model - model to be used
            # messages - list of messages, each message has a role and content
                # role - assistant, user, system
                # content - the content of the message
            # temperature - controls the randomness of the output, higher value means more random, lower value means more deterministic (0-2, 0.7 is a good default)
            # top_p - controls the diversity of the output, higher value means more diverse, lower value means more focused 
            # max_tokens - controls the maximum number of tokens in the output (puts a hard limit on LLM response)
            # stop - controls the stopping criteria for the output, can be a string or a list of strings
            # stream - controls whether to stream the output or not, if True, the output will be streamed in chunks, if False, the output will be returned as a whole
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=self.messages
        )
        
        # response.choices - > list of choices(LLM may reply with multiple choices), each choice has a message with content
        content =  response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": content})
        self.total_tokens += response.usage.total_tokens
        return content

    def chat(self):
        print("Welcome to the chatbot! Type 'exit' to quit.")
        while True:
            query = input("You: ")
            if query.lower() == 'exit':
                print("Goodbye!")
                break
            response = self.bot(query)
            print(f"Bot: {response}")

    def report(self):
        for message in self.messages:
            print(message)
        print(f"Total tokens used: {self.total_tokens}")

def main():
    chat_bot = ChatBot()
    chat_bot.chat()
    chat_bot.report()

if __name__ == '__main__':
    main()