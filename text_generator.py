from nltk.tokenize import WhitespaceTokenizer
import nltk
from collections import Counter


#f = open("/Users/aleksander/Downloads/corpus.txt", "r", encoding="utf-8")   # str


with open(input(), "r", encoding="utf-8") as file:
    file_content = file.readlines()


file_as_str = "".join(file_content)
tk = WhitespaceTokenizer()
tokens = tk.tokenize(file_as_str)
bigrams_tuple = tuple(nltk.bigrams(tokens))

# print(list(nltk.bigrams(tokens)))

markov_model_dict = {}

for head, tail in bigrams_tuple:
    markov_model_dict.setdefault(head, []).append(tail)


for key in markov_model_dict:
    markov_model_dict[key] = Counter(markov_model_dict[key])


print("Number of bigrams:", len(bigrams_tuple))
print()


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
            head = bigrams_tuple[int(bigram_index)][0]
            tail = bigrams_tuple[int(bigram_index)][1]
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
        for tail, counter in markov_model_dict[markov_head].items():
            print(f"Tail: {tail}\tCount: {counter}")


while True:
    markov_tails_by_head()
