with open("output.txt",'wt')as fh: #first created the file
    content1=(input("Enter text to write  to the file:")) # Taking input from the user
    fh.write(str(content1+"\n"))
    print("Data Successfully written to 'output.txt'")
with open("output.txt",'at') as fh:
    content2 = (input("Enter additional text to append:")) #appending additional data from the user
    fh.write(str(content2))
    print("Data successfully appended")
    print("File content of output.txt:")
with open("output.txt", 'rt') as fh:
    content1=fh.readline()
    print(content1)
    content2 = fh.readline()
    print(content2)
