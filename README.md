                                       Word Length Analyzer (Python)
Overview 

This is a simple Python program that takes a line of text as input and calculates:

Length of each word
Total length of the text (including spaces)

It also allows the user to repeat the process multiple times until they choose to exit.

Features
Splits input text into individual words
Calculates and displays length of each word
Shows total length of the full text (with spaces)
User-friendly loop to continue or exit the program

Technologies Used
Python 3
Built-in libraries (sys)
Program Structure
Function: wordlen(lineoftext)
Handles logic for word splitting and length calculation
Main Loop:
Continuously takes user input until exit condition

▶️ How to Run
Make sure Python is installed on your system
Save the file as word_length.py
Open terminal or command prompt
Run the program:
python word_length.py

💻 Sample Output
Enter Your line of text: Hello World
------------------------------
    len(Hello) is 5
    len(World) is 5
--------------------------------------------------
Total length of Text with space: = 11
--------------------------------------------------
Due Your want to Try again for another line of text Y/N:
🔁 Program Flow
User enters a line of text
Program splits the text into words
Displays length of each word
Shows total length including spaces
Prompts user to continue or exit
⚠️ Validation
Empty input is considered invalid
Program will prompt again if input is blank
📌 Future Improvements
Ignore punctuation
Count number of words
Display longest and shortest word
GUI version using Tkinter

👨‍💻 Author

Rahul Gupta