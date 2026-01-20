def read_words(sentences: list):
    word_count = {}

    for sentence in sentences:
        words = sentence.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count


def find_max_word(word_count: dict):
    max_freq = 0
    max_word = None

    for word, count in word_count.items():
        if count > max_freq:
            max_freq = count
            max_word = word

    print(max_word, max_freq)


sentences = [
    "hello world",
    "hello python world",
    "hello"
]

data = read_words(sentences)
find_max_word(data)