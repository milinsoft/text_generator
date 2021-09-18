import re

from nltk.tokenize import WhitespaceTokenizer
import nltk
from collections import Counter
import random


def obtain_dataset_from_file():
    with open(input(), "r", encoding="utf-8") as file:
    #with open("/Users/aleksander/Downloads/corpus.txt", "r", encoding="utf-8") as file:
        file_content = file.readlines()
    return "".join(file_content)


def token_by_index() -> "requested token, error message, or index":
    token_index = input()
    try:
        token_index = int(token_index)
    except ValueError:
        if isinstance(token_index, str):
            if token_index == "exit":
                exit()
            else:
                print("Type Error. Please input an integer.")
                return token_by_index()
    else:
        if token_index > len(tokens):
            print("Index Error. Please input an integer that is in the range of the corpus.")
            return token_by_index()
        else:
            print(tokens[int(token_index)])


def bigrams_by_index() -> "requested bigram's head and tail, error message, or index":
    bigram_index = input()
    try:
        bigram_index = int(bigram_index)
    except ValueError:
        if isinstance(bigram_index, str):
            if bigram_index == "exit":
                exit()
            else:
                print("Type Error. Please input an integer.")
                return bigrams_by_index()
    else:
        if bigram_index > len(bigrams_tuple):
            print("Index Error. Please input an integer that is in the range of the corpus.")
            return bigrams_by_index()
        else:
            head = bigrams_tuple[bigram_index][0]
            tail = bigrams_tuple[bigram_index][1]
            print(f"Head: {head}\tTail: {tail}")


def markov_tails_by_head() -> "all the possible tails and their corresponding counts.":
    markov_head = input()
    if markov_head == "exit":
        exit()
    elif markov_head not in markov_model_dict:
        print(f"Head: {markov_head}")
        print("Key Error. The requested word is not in the model. Please input another word.")
        return markov_tails_by_head()
    else:
        print(f"Head: {markov_head}")
        for bigram_tail, counter in markov_model_dict[markov_head].items():
            print(f"Tail: {bigram_tail}\tCount: {counter}")


def generate_pseudosentence() -> "pseudo sentence from 10 tokens":
    random_head = "".join(random.choices(list(markov_model_dict.keys())))
    sentence_list = [random_head]
    while len(sentence_list) != 10:
        current_tail = sentence_list[-1]
        potential_tails = [key for key in markov_model_dict[current_tail].keys()]
        tails_weights = [weight for weight in markov_model_dict[current_tail].values()]
        new_tail = "".join(random.choices(potential_tails, weights=tails_weights))
        sentence_list.append(new_tail)
    sentence_str = " ".join(sentence_list)
    print(sentence_str)


def set_initial_head():
    random_head = "".join(random.choices(list(markov_model_dict.keys())))
    template = r"\A[A-Z][a-z]+$"
    if re.match(template, random_head):
        return random_head
    else:
        return set_initial_head()


def lastword_check():
    ...


def generate_readlsentence():
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
            template = r"[A-Za-z]+[\.?!]{1,}$"
            if re.match(template, lastword):
                break
        else:
            continue

    sentence_str = " ".join(sentence_list)
    print(sentence_str)


def generate_pseudotext() -> "10 pseudo-sentences with 10 tokens each":
    for _ in range(10):
        generate_pseudosentence()


def generate_realtext():
    for _ in range(10):
       generate_readlsentence()


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
