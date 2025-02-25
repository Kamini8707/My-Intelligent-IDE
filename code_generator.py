from openai import OpenAI
from config import OPENAI_API_KEY

def generate_code(prompt):
    try:
        # Initialize the OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a programming expert. Generate clean, efficient, and well-documented code."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"# Error generating code: {str(e)}\n# Please make sure your OpenAI API key is set correctly."
