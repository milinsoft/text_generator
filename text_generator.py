from nltk.tokenize import WhitespaceTokenizer
import nltk


# f = open("/Users/aleksander/Downloads/corpus.txt", "r", encoding="utf-8")   # str


f = open(input(), "r", encoding="utf-8")   # str

a = f.readlines()
a = "".join(a)
tk = WhitespaceTokenizer()
tokens = tk.tokenize(a)
bigrams_tuple = tuple(nltk.bigrams(tokens))


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


while True:
    bigrams_by_index()
