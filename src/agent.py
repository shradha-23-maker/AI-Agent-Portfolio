
import ollama

print("===== My AI Agent =====")
print("Type 'exit' to stop the agent.")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        print("AI Agent: Goodbye!")
        break

    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    print("\nAI Agent:", response["message"]["content"])