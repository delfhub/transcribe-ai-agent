import ollama

def test_connection():
    print("sending request to ollama...")

    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': 'say "hello world" if you can hear me',
        },
    ])

    print("response from ollama: ", response['message']['content'])

def test_structured_role():
    response = ollama.chat(model='llama3.2', messages=[
        {
            'role': 'system',
            'content': 'You are a sarcastic Unix terminal. Respond briefly and mock the user for not using sudo.',
        },
        {
            'role': 'user',
            'content': 'How do I check my disk space?',
        },
    ])
    
    print("Response:", response['message']['content'])

test_structured_role()

if __name__ == "__main__":
    # test_connection()
    test_structured_role()