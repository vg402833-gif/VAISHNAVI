with open("textfile_of_task1",'wt') as fh: # first created a file than written the content in the file
    fh.write("This is a sample text file\nIt contains multiple lines") # content of the file
try:
    print("Reading file content")
    with open("textfile_of_task1",'rt') as fh:
        line1=fh.readline()
        line2 = fh.readline()
        print(f"line1:{line1}") #prints the line 1 content
        print(f"line2:{line2}") # prints thw line2 content
except:
        print("The file 'textfile_of_task1' was not found")

