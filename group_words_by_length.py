def group_by_length(words):
    grouped_words ={}
    for word in words:
        word_len = len(word)
        if word_len in grouped_words:
            grouped_words[word_len].append(word)
        else:
            grouped_words[word_len] = [word]
    return(grouped_words)


words = ["apple", "bat", "ball", "cat", "doll", "elephant"]
print(group_by_length(words))