"""
LLM Benchmark Script
Generates a challenging question, queries multiple LLMs, and ranks their responses.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from anthropic import Anthropic
from IPython.display import Markdown, display

# Load environment variables from .env file
load_dotenv(override=True)

# Print the key prefixes to help with any debugging

openai_api_key = os.getenv('OPENAI_API_KEY')
anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')
deepseek_api_key = os.getenv('DEEPSEEK_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')

# Display which API keys are configured (for debugging)
if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    print("OpenAI API Key not set")
    
if anthropic_api_key:
    print(f"Anthropic API Key exists and begins {anthropic_api_key[:7]}")
else:
    print("Anthropic API Key not set (and this is optional)")

if google_api_key:
    print(f"Google API Key exists and begins {google_api_key[:2]}")
else:
    print("Google API Key not set (and this is optional)")

if deepseek_api_key:
    print(f"DeepSeek API Key exists and begins {deepseek_api_key[:3]}")
else:
    print("DeepSeek API Key not set (and this is optional)")

if groq_api_key:
    print(f"Groq API Key exists and begins {groq_api_key[:4]}")
else:

# ============================================================================
# STEP 1: Generate a challenging question using OpenAI
# ============================================================================
    print("Groq API Key not set (and this is optional)")

request = "Please come up with a challenging, nuanced question that I can ask a number of LLMs to evaluate their intelligence. "
request += "Answer only with the question, no explanation."
messages = [{"role": "user", "content": request}]

openai = OpenAI()
response = openai.chat.completions.create(
    mof"\n🤔 Generated Question:\n{question}\n")

# ============================================================================
# STEP 2: Query multiple LLMs with the same question
# ============================================================================

competitors = []
answers = []
messages = [{"role": "user", "content": question}]

# Query OpenAI GPT-5-nano
model_name = "gpt-5-nano"
response = openai.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
competitors.append(model_name)
answers.append(answer)
print(f"✓ Got response from {model_name}"ices[0].message.content

#display(Markdown(answer))
competitors.append(model_name)
# Query Anthropic Claude
model_name = "claude-sonnet-4-5"
claude = Anthropic()
response = claude.messages.create(model=model_name, messages=messages, max_tokens=1000)
answer = response.content[0].text
competitors.append(model_name)
answers.append(answer)
print(f"✓ Got response from {model_name}"
#display(Markdown(answer))
competitors.append(model_name)
answers.append(answer)

gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.5-flash"
# Query Google Gemini
gemini = OpenAI(api_key=google_api_key, base_url="https://generativelanguage.googleapis.com/v1beta/openai/")
model_name = "gemini-2.5-flash"
response = gemini.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
competitors.append(model_name)
answers.append(answer)
print(f"✓ Got response from {model_name}")

# Query local Ollama model
ollama = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
model_name = "llama3.2"
response = ollama.chat.completions.create(model=model_name, messages=messages)
answer = response.choices[0].message.content
competitors.append(model_name)
answers.append(answer)
print(f"✓ Got response from {model_name}")

print(f"\n📊 Collected {len(competitors)} responses")

# Print each competitor's answer for review
print("\n" + "="*80)
print("COLLECTED RESPONSES")
print("="*80)
for competitor, answer in zip(competitors, answers):
    print(f"\n--- {competitor} ---

together = ""
for index, answer in enumerate(answers):
    together += f"# Response from competitor {index+1}\n\n"
    together += answer + "\n\n"

print(together)

judge = f"""You are judging a competition between {len(competitors)} competitors.
Each model has been given this question:

{question}

Your job is to evaluate each response for clarity and strength of argument, and rank them in order of best to worst.
Respond with JSON, and only JSON, with the following format:
{{"results": ["best competitor number", "second best competitor number", "third best competitor number", ...]}}
# ============================================================================
# STEP 3: Prepare responses for judging
# ============================================================================

together = ""
for index, answer in enumerate(answers):
    together += f"# Response from competitor {index+1}\n\n"
    together += answer + "\n\n"

# ============================================================================
# STEP 4: Use OpenAI as judge to rank the responses
# ============================================================================h the JSON with the ranked order of the competitors, nothing else. Do not include markdown formatting or code blocks."""

print(judge)

judge_messages = [{"role": "user", "content": judge}]


openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-mini",
# Send judging request to OpenAI
judge_messages = [{"role": "user", "content": judge}]
openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-mini",
    messages=judge_messages,
)
results = response.choices[0].message.content

# ============================================================================
# STEP 5: Display final rankings
# ============================================================================

# Parse JSON results and display rankings
results_dict = json.loads(results)
ranks = results_dict["results"]

print("\n" + "="*80)
print("FINAL RANKINGS")
print("="*80)
for index, result in enumerate(ranks):
    competitor = competitors[int(result)-1]
    medal = ["🥇", "🥈", "🥉"][index] if index < 3 else "  "
    print(f"{medal} 