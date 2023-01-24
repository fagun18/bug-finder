import os
import subprocess

def find_bugs(path):
    # Run static code analysis tool
    result = subprocess.run(['pylint', path], capture_output=True, text=True)

    # Print the output of the tool
    print(result.stdout)
    
    # Check for the presence of the string "Fatal"
    if "Fatal" in result.stdout:
        print("Fatal error found.")
    else:
        print("No fatal errors found.")

if __name__ == '__main__':
    path = "example.py"
    find_bugs(path)
