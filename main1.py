# Import the load_dotenv function from the dotenv module to read environment variables
from dotenv import load_dotenv
# Load environment variables from the .env file and override existing ones
load_dotenv(override=True)

# Import the os module to access environment variables
import os
# Retrieve the OPENAI_API_KEY from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Check if the API key exists and print a confirmation message, otherwise print an error message
if openai_api_key:
    # Print confirmation message showing the first 8 characters of the API key
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    # Print error message if API key is not found
    print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

# Import the OpenAI client class
from openai import OpenAI
# Initialize the OpenAI client (uses OPENAI_API_KEY from environment)
client = OpenAI()

# Create a list containing the user's message
messages = [{"role": "user", "content": "What is 2+2?"}]
# Send a request to OpenAI's chat completion API with the gpt-4.1-nano model
response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=messages
)

# Extract and print the content of the first response choice
print(response.choices[0].message.content)

# And now - let's ask for a question:

prompt = "Please propose a hard, challenging question to assess someone's IQ. Respond only with the question."
messages = [{"role": "user", "content": prompt}]

# ask it - this uses GPT 4.1 mini, still cheap but more powerful than nano

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

question = response.choices[0].message.content

print(question)

# form a new messages list
messages = [{"role": "user", "content": question}]

# Ask it again

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=messages
)

answer = response.choices[0].message.content
print(answer)

