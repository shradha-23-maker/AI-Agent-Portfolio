from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "What is an AI Agent?"
        }
    ]
)

print(response["message"]["content"])
