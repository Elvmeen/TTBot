import openai
import os

# Use your OpenAI API key stored as an environment variable
api_key = os.getenv("OPENAI_API_KEY")  # Ensure this variable is set in your environment

if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    exit(1)

openai.api_key = api_key

try:
    # Example test prompt
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you are using it
        messages=[
            {"role": "user", "content": "Write a short tweet about artificial intelligence."}
        ]
    )

    # Extract and print the response
    print("Generated tweet:", completion.choices[0].message['content'].strip())
except Exception as e:
    print(f"Error using OpenAI API: {e}")