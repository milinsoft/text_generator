def obtain_dataset_from_file() -> str:
    with open(input(), "r", encoding="utf-8") as file:
        file_content = file.readlines()
    return "".join(file_content)


def create_markov_model() -> dict:
    """1) obtaining file content in a str. var.,
    2) creates the trigrams_list of tokens,
    3) creates the dictionary concatinating the first two tokens of trigram as a dictionary key
    4) filling out markov_chain dict with all tokens that follows tokens, matching dictionary keys in a trigrams_list"""

    file_as_str = obtain_dataset_from_file()
    tk = WhitespaceTokenizer()  # instanse of WhitespaceTokenizer class
    tokens = tk.tokenize(file_as_str)
    trigrams_list = list(nltk.trigrams(tokens))
    markov_chain = {}

    for head_1, head_2, tail in trigrams_list:
        head = "  ".join([head_1, head_2])
        markov_chain.setdefault(head, list()).append(tail)

    for key in markov_chain:
        markov_chain[key] = dict(Counter(markov_chain[key]))
    return markov_chain


def set_initial_head() -> str:
    """Obtains the 'first_word' which matches regex template to start the sentence"""
    first_word = random.choices(list(markov_model_dict.keys()))
    template = r"(\A[A-Z][a-z]+  [A-Za-z]+)$"
    if re.match(template, "".join(first_word)):
        return "".join(first_word)
    else:
        return set_initial_head()


def generate_realsentence() -> str:
    """1) calls set_initial_head() function to obtain the first token to start the pseudo sentence
    2) looking for the next token for the pseudo sentence based on a double space concatination of the last two tokens until minimal length of the sentence, equal to 5 tokens satisfied
    3) checks if the last token ends with a dot, a question mark or an exclamation mark
    and terminates the loop if this condition is satisfied, continuing the loop checking every next step otherwise"""

    initial_head = set_initial_head().split()
    sentence_list = [head for head in initial_head]

    while True:
        current_tail = "  ".join([sentence_list[-2], sentence_list[-1]])
        potential_tails = [key for key in markov_model_dict[current_tail].keys()]
        tails_weights = [weight for weight in markov_model_dict[current_tail].values()]
        new_tail = "".join(random.choices(potential_tails, weights=tails_weights))
        sentence_list.append(new_tail)
        if len(sentence_list) >= 5:
            if sentence_list[-1][-1] in {"!", ".", "?"}:
                break
    print(" ".join(sentence_list))


def generate_realtext() -> "prints statements":
    """Calls generate_realsentence() function 10 times in order to print 10 pseudo sentences"""
    for _ in range(10):
        generate_realsentence()


if __name__ == '__main__':
    import re
    from nltk.tokenize import WhitespaceTokenizer
    import nltk
    from collections import Counter
    import random
    markov_model_dict = create_markov_model()
    generate_realtext()
