from openai import OpenAI
from config import OPENAI_API_KEY

def generate_docs(code):
    try:
        # Initialize the OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a documentation expert. Generate comprehensive documentation."},
                {"role": "user", "content": f"Generate documentation for this code:\n\n{code}"}
            ]
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error generating documentation: {str(e)}"
