
import argparse

def summarize_file(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            # For simplicity, we'll return the first 100 characters as a summary.
            # In a real-world scenario, a more sophisticated summarization algorithm would be used.
            summary = content[:500] + "..." if len(content) > 500 else content
            return f"File summary: {summary}"
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Summarize the content of a file.")
    parser.add_argument("file_path", type=str, help="The path to the file to summarize.")
    args = parser.parse_args()
    print(summarize_file(args.file_path))
