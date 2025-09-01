def word_count(file):
    with open(file) as f:
        text_contents = f.read()
    words = text_contents.split()
    num_words = len(words)
    return num_words

def char_count(file):
    with open(file) as f:
        text_contents = f.read()
    letters = {}
    for char in text_contents:
        if char.isalpha():
            char = char.lower()
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters