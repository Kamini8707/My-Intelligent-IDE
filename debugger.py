from openai import OpenAI
from config import OPENAI_API_KEY
import ast

def debug_code(code):
    try:
        # Check if code is valid Python syntax
        try:
            ast.parse(code)
        except SyntaxError as e:
            return f"Syntax Error: {str(e)}"

        # Initialize the OpenAI client
        client = OpenAI(api_key=OPENAI_API_KEY)
        
        debug_prompt = f"""Analyze this Python code and provide debugging information:

Code to analyze:
{code}

Please provide:
1. Potential bugs or issues
2. Code improvement suggestions
3. Performance considerations
4. Best practices recommendations"""

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a Python debugging expert. Analyze code for bugs and improvements."},
                {"role": "user", "content": debug_prompt}
            ]
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"Error in debugging: {str(e)}"
