if __name__ == "__main__":
    wordFile = open("words.txt", "r")
    Lines = wordFile.readlines()
    for line in Lines:
        print(line)
