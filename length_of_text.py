#Program to find length of each word from line of Text

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

#main Program
while True:
    #Checking criteria of Line of Text
    lineoftext = input("Enter Your line of text: ").strip()
    if len(lineoftext) <= 0 :
        print("{} is a Invalid Sentence".format(lineoftext))
    else:
        wordlen(lineoftext) #function call