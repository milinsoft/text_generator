import re

from nltk.tokenize import WhitespaceTokenizer
import nltk
from collections import Counter
import random


def obtain_dataset_from_file():
    with open(input(), "r", encoding="utf-8") as file:
    # with open("/Users/aleksander/Downloads/corpus.txt", "r", encoding="utf-8") as file:
        file_content = file.readlines()
    return "".join(file_content)


def set_initial_head():
    random_head = "".join(random.choices(list(markov_model_dict.keys())))
    template = r"\A[A-Z][a-z]+$"
    if re.match(template, random_head):
        return random_head
    else:
        return set_initial_head()


def lastword_check(lastword):
    template = r"[A-Za-z]+[\.?!]{1,}$"
    return re.match(template, lastword)


def generate_realsentence():
    # don't forget to rename variables
    initial_head = set_initial_head()
    sentence_list = [initial_head]

    while True:
        current_tail = sentence_list[-1]
        potential_tails = [key for key in markov_model_dict[current_tail].keys()]
        tails_weights = [weight for weight in markov_model_dict[current_tail].values()]
        new_tail = "".join(random.choices(potential_tails, weights=tails_weights))
        sentence_list.append(new_tail)

        if len(sentence_list) >= 5:
            lastword = "".join(sentence_list[-1])
            if lastword_check(lastword):
                break
            else:
                continue
    sentence_str = " ".join(sentence_list)
    print(sentence_str)


def generate_realtext():
    for _ in range(10):
        generate_realsentence()


if __name__ == '__main__':
    print()
    # obtaining dataset from file
    file_as_str = obtain_dataset_from_file()
    tk = WhitespaceTokenizer()
    tokens = tk.tokenize(file_as_str)
    bigrams_tuple = tuple(nltk.bigrams(tokens))
    markov_model_dict = {}
    for head, tail in bigrams_tuple:
        markov_model_dict.setdefault(head, list()).append(tail)

    for key in markov_model_dict:
        markov_model_dict[key] = Counter(markov_model_dict[key])

    generate_realtext()
