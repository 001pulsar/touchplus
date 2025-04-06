
# need feature updates as well

import os
import sys

# main function
def fileOpener():
    file = open(filename, "r")
    for line in file:
        print(line)
    file.close()

# checking arguments format
if ((len(sys.argv)) < 2):
    print("Enter filename. Usage: program.py filename.txt")
    sys.exit()
elif ((len(sys.argv)) > 2):
    print("Extra arguments detected. Usage: program.py filename.txt")
    sys.exit()
# checking if file exists
else:
    filename = sys.argv[1]
    if os.path.exists(filename):
        fileOpener()
    else:
        print("File doesn't exist.")
        choice = input("Do you want to create the file (y/n): ")
        if (choice == "y"):
            file = open(filename, "w")
            print("File created successfully!")
            fileOpener()
        elif (choice == "n"):
            print("OK")
            sys.exit()
        else:
            print("Invalid input")
            sys.exit()
