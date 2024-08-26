from openai import OpenAI
client = OpenAI(api_key="sk-bN8dGa7YArA7tXjjqgkjXLya_dKh2anbEVPrQEBNhXT3BlbkFJsRVDhvN6kPSdYTEtXNMkF1dCsN1kk2xHyERpAKtiYA",)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message.content)