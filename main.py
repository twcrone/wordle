import random
import sys


def guess(patterns):
    best_options = []
    word_file = open("words.txt", "r")
    past_file = open("past.txt", "r")
    lines = word_file.readlines()
    past_words = past_file.readlines()
    lines = remove_strings_from_list(lines, past_words)
    if len(patterns) == 0:
        count = len(lines)
        r = random.randrange(count)
        return lines[r]

    for line in lines:
        line = line.strip()
        if is_match_for(line, patterns):
            best_options.append(line)
    if len(best_options) == 0:
        return "?????"
    r = random.randrange(len(best_options))
    return best_options[r]

def remove_strings_from_list(list1, list2):
    """Removes strings from list1 that are present in list2."""
    result = [x for x in list1 if x not in list2]
    return result

def is_match_for(word, patterns):
    for pattern in patterns:
        if pattern.startswith("-"):
            if not excluded(word, pattern[1:]):
                return False
        elif not matches(word, pattern):
            return False
    return True


def matches(word, pattern):
    for i in range(len(pattern)):
        letter = pattern[i]
        if letter == "_":
            continue
        if letter.isupper() and not letter.lower() == word[i].lower():
            return False
        elif letter.islower() and not included_but_not_at_index(word, letter, i):
            return False
    return True


def included_but_not_at_index(word, letter, index):
    return letter in word and word[index] != letter


def excluded(word, excludes):
    for i in range(len(excludes)):
        if excludes[i] in word:
            return False

    return True


if __name__ == "__main__":
    print(guess(sys.argv[1:]))
