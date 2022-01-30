import sys

if __name__ == "__main__":
    word = "COULD" if len(sys.argv) < 2 else sys.argv[1]
    print(word)
    # wordFile = open("words.txt", "r")
    # Lines = wordFile.readlines()
    # for line in Lines:
    #     print(line)
