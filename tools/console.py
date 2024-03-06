import sys
from rich.console import Console
from rich.markdown import Markdown

def main(prompt, input_data=None):
    console = Console()
    console.print(Markdown(prompt))
    if input_data:
        console.print(Markdown("### Input Data:"))
        console.print(Markdown(input_data))

def process_logic(item, console):
    # Example processing logic function
    # Use console.print() for any output
    result = f"Processed item {item}"  # Placeholder for actual logic result
    console.print(Markdown(result))

if __name__ == "__main__":
    console = Console()

    # Check if there's input from a pipe or redirection
    if not sys.stdin.isatty():
        input_data = sys.stdin.read()
        if len(sys.argv) > 1:
            prompt = sys.argv[1]
        else:
            prompt = "Default prompt, with piped or redirected script"
    else:
        if len(sys.argv) > 1:
            prompt = sys.argv[1]
            input_data = None
        else:
            console.print("Usage: python3 stream.py 'prompt' < script.py or | cat script.py")
            sys.exit(1)

    main(prompt, input_data)

