from nltk.tokenize import WhitespaceTokenizer
import ast
# from ast import literal_eval

#f = open("/Users/aleksander/Downloads/corpus.txt", "r", encoding="utf-8")   # str

f = open(input(), "r", encoding="utf-8")   # str

a = f.readlines()
a = "".join(a)
tk = WhitespaceTokenizer()
tokens = tk.tokenize(a)

print("Corpus statistics")
print("All tokens:", len(tokens))
print("Unique tokens:", len(set(tokens)))
print()


def token_by_index():
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


while True:
    token_by_index()

# check with ranges and check type
