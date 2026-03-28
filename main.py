import sys
from cli.commands import analyze_code

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py analyze <file.py>")
    else:
        command = sys.argv[1]
        file_path = sys.argv[2]

        if command == "analyze":
            analyze_code(file_path)