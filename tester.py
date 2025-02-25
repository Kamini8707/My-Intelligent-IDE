from openai import OpenAI
from config import OPENAI_API_KEY

def run_tests(code):
    try:
        # Initialize the OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python testing expert. Generate comprehensive test cases."},
                {"role": "user", "content": f"Generate unit tests for this code:\n\n{code}"}
            ]
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error in testing: {str(e)}"
