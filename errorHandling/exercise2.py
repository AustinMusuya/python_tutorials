

try:
    f = open("text.txt", "a")
    f.write("\nNew content")
    f.close()

    f = open("text.txt", "r")
    print(f.readlines())
    f.close()
except FileNotFoundError as e:
    print("File not found!")
