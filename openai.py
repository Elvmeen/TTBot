from openai import OpenAI
client = OpenAI(  
  api_key="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")

client = OpenAI()
completion = client.chat.completions.create(
    model="gpt-4o",
    store=True,
    messages=[
        {"role": "user", "content": "write a haiku about ai"}
    ]
)
