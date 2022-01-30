import sys


def find_best_option(pattern):
    best_word = ""
    best_score = 0
    word_file = open("words.txt", "r")
    lines = word_file.readlines()
    for line in lines:
        line = line.strip()
        line_score = score(line, pattern)
        # print(line + " (" + str(line_score) + ")")
        if line_score > best_score:
            best_score = line_score
            best_word = line
    return best_word + " (" + str(best_score) + ")"


def score(word, pattern):
    if len(word) != len(pattern):
        return -1
    result = 0
    for i in range(len(word)):
        w = word[i]
        p = pattern[i]
        if p.isupper() and w == p.lower():
            result += 3
        elif p in word:
            result += 1

    return result


if __name__ == "__main__":
    arg = "COULD" if len(sys.argv) < 2 else sys.argv[1]
    print(arg)
    print(find_best_option(arg))
