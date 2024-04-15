import openai
import sys
import os
from rich.console import Console
from rich.markdown import Markdown

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 gpt.py <system_prompt_text_or_file> <user_prompt_text_or_file>")
        sys.exit(1)

    system_prompt = ""
    if os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], "r") as file:
            system_prompt = file.read()
    else:
        system_prompt = sys.argv[1]

    user_prompt = ""
    if os.path.isfile(sys.argv[2]):
        with open(sys.argv[2], "r") as file:
            user_prompt = file.read()
    else:
        user_prompt = sys.argv[2]

    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        client = openai.OpenAI()
        console = Console()
        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        answer = response.choices[0].message.content
        if answer is not None:
            console.print("")
            console.print(Markdown(answer))
        else:
            console.print("No answer received")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
