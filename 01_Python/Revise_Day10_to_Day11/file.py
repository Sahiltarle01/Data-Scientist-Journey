# Object Oriented Programing (OOP)
# Q.1 Create a file and write your name into it
with open("data.txt", "w") as file:
    file.write("Sahil Tarle")
print("data.txt file created successfully!")

# Q.2 Read and display the contents of data.txt
with open("data.txt", "r") as file:
    content = file.read()
print("Contents of data.txt:")
print(content)

# Q.3 Append your college name to data.txt.
with open("data.txt", "a") as file:
    file.write("\nSanjivani University, Kopargaon")
print("College name appended successfully!")

# Q.4 Count the total number of characters in a file
with open("data.txt", "r") as file:
    content = file.read()
count = len(content)
print("Total number of characters:", count)

# Q.5 Count the total number of words in a file
with open("data.txt", "r") as file:
    content = file.read()
word_count = len(content.split())
print("Total number of words:", word_count)

# Q.6 Count the total number of lines in a file.
with open("data.txt", "r") as file:
    lines = file.readlines()
line_count = len(lines)
print("Total number of lines:", line_count)

# Q.7 Copy the contents of data.txt into a new file named backup.txt.
with open("data.txt", "r") as source:
    content = source.read()
with open("backup.txt", "w") as destination:
    destination.write(content)
print("Contents copied successfully!")
 
# Q.8 Search for a specific word in a file and display whether it exists.
word = input("Enter the word to search: ")
with open("data.txt", "r") as file:
    content = file.read()
if word in content:
    print("Word found in the file.")
else:
    print("Word not found in the file.")
    
# Q.9 Replace a word in a file
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
with open("data.txt", "r") as file:
    content = file.read()
content = content.replace(old_word, new_word)
with open("data.txt", "w") as file:
    file.write(content)
print("Word replaced successfully!")

# Q.10 Display only the lines that contain the word "Python"
with open("data.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())