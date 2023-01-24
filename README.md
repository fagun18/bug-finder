# Software bug-finder
A simple Python script that can be used to find bugs in a software application:

This script uses the subprocess library in Python to run a static code analysis tool pylint which analyze the source code for potential bugs and coding standard violations, the script captures the output of the tool and prints it.

It checks for the presence of the string "Fatal" in the output, indicating a fatal error and print out a message accordingly.
It's important to note that this is just an example and you can use other tools as well such as Flake8, mypy and Pyflakes

It's also important to note that this script is just a skeleton and it doesn't include the actual implementations of the methods, these methods should be implemented by the tester according to the software under test.

Additionally, you may want to consider using a more robust bug finding tools like Pydocstyle, Bandit and McCabe for finding bugs in the software applications
