from openai import OpenAI
from config import OPENAI_API_KEY

def test_code():
    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python expert. Generate code for a factorial function."},
                {"role": "user", "content": "Write a Python function to calculate factorial."}
            ],
            max_tokens=100,
        )
        print(response.choices[0].message.content.strip())

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_code()
