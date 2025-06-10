#File Opening and setting variable.
try:
    with open('sample.txt', 'r') as file1:
        reading_file=file1.readlines()

# Error handling if file is empty
    if not reading_file: print("'sample.txt' is empty")

    n=0
    for i in reading_file :
        print("Line",n+1,":",i)
        n=(n+1)

# Error handling if file does not exist
except FileNotFoundError:
    print("Error:File 'sample.txt' is not found")