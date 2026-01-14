vowels = set('aeiou')
word = input("provide a word t0 search for vowels: ")
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)
