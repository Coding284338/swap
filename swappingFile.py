def swapFileData():
    input1 = input("what is the name of the first file you want to swap?")
    input2 = input("what is the name of the second file you want to swap?")
    #opening input1 in read mode as a   
    with open(input1,'r') as a:
        #read the contents of file a and store it in data_a
        data_a = a.read()

    with open(input2,'r') as b:
        data_b = b.read()

    with open(input1,'w') as a:
        a.write(data_b)

    with open(input2,'w') as b:
        b.write(data_a)

swapFileData()