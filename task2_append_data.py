with open('output.txt', 'w') as f:

    # Asking for user input 1:
    writing = f.write(input("Enter text to write to the file:") + '\n')
    print("data successfully written to file",writing)
 
with open('output.txt', 'a') as A:

    # Asking for user input 2:
    append = A.write(input("Enter additional text to append to the file: ") + '\n' )
    print("data successfully appeneded to file",append)

# Output
with open('output.txt', 'r+') as R:
    read = R.readlines()
    print("final content of output text:",read)