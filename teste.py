import nltk

tokens = nltk.word_tokenize("estou testando o nltk", "portuguese")

for token in tokens:
    print("token:", token)