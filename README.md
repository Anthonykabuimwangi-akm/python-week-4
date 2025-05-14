File Read & Write Challenge and Error Handling Lab
Overview
This repository contains two Python programs that demonstrate file handling capabilities in Python: one for reading and writing files and another for handling errors when trying to read a specified file.

Contents
file_read_write.py: A program that reads a text file, modifies its content, and writes it to a new file.
error_handling_lab.py: A program that prompts the user for a filename and manages errors if the file does not exist or cannot be read.
Requirements
Python 3.x installed on your machine.
How to Run the Programs
File Read & Write Program

Place a text file in the same directory as file_read_write.py (you can name it example.txt or any name you prefer).
Open the terminal or command prompt.
Run the following command:
bash

python file_read_write.py
The program will create a modified version of the file named modified_example.txt, converting all text to uppercase.
Error Handling Lab

Open the terminal or command prompt.
Run the following command:
bash

python error_handling_lab.py
You will be prompted to enter a filename. Type the name of the file you want to read.
If the file exists, its content will be displayed; if not, an error message will be shown.
Example
File Read & Write Program
Input: A text file named example.txt containing:

Hello, World!
This is a text file.
Output: A text file named modified_example.txt containing:

HELLO, WORLD!
THIS IS A TEXT FILE.
Error Handling Lab
If you enter a filename that does not exist, you will see:

Error: The file <filename> does not exist.# python-week-4
