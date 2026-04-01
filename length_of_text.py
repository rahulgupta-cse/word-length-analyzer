#Program to find length of each word from line of Text

#main Program
while True:
    #Checking criteria of Line of Text
    lineoftext = input("Enter Your line of text: ").strip()
    if len(lineoftext) <= 0 :
        print("{} is a Invalid Sentence".format(lineoftext))
    else:
        wordlen(lineoftext) #function call