from random_word import RandomWords
import random


def generate_wordlist():
    r = RandomWords()

    words = r.get_random_words(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minDictionaryCount=1,
                               maxDictionaryCount=10, minLength=5, maxLength=10, sortBy="alpha", sortOrder="asc",
                               limit=40)

    f = open("words.txt", "w+")
    for i in range(len(words)):
        f.write("{}\n".format(words[i]))

    f.close()


def get_random_word(min_word_length):
    """Get a random word from the wordlist"""
    num_words_processed = 0
    curr_word = None
    generate_wordlist()

    with open("words.txt", "r") as file:
        for word in file:
            if '-' in word:
                continue
            if '(' in word or ')' in word:
                continue

            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed +=1
            if random.randint(1,  num_words_processed) == 1:
                curr_word = word

    return curr_word
