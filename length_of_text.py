#Program to find length of each word from line of Text


#import sys for exit out of program
import sys 


#Defing the function
def wordlen(lineoftext):
    #logic to find the length
    word = lineoftext.split()
    print("-" * 30)
    for i in word:
        print("\tlen({}) is {}".format(i,len(i)))
    print("-" * 50) #decoration part
    print("Total length of Text with space: =",len(lineoftext))
    print("-" * 50)

    #Logic here to stop or continue the Program
    tryagain = input("Due Your want to  Try again for another line of text Y/N:").lower()
    if tryagain == 'n':
        print("Program Exited Successfully")
        sys.exit()

#main Program
while True:
    #Checking criteria of Line of Text
    lineoftext = input("Enter Your line of text: ").strip()
    if len(lineoftext) <= 0 :
        print("{} is a Invalid Sentence".format(lineoftext))
    else:
        wordlen(lineoftext) #function call