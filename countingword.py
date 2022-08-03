def countingword():
    #ask the users to enter the file name whose words need to be counted
    filename = input("enter the file name whose words need to be counted: ")

    numberofwords = 0

    #opening the given file in read mode
    file = open(filename,"r")

    for i in file:
        words = i.split()
        numberofwords += len(words)
    print("number of words in file are ",numberofwords)
countingword()



