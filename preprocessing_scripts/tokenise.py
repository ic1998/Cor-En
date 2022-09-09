#tokenises sentences

#import libraries
import nltk

#read file
def read_file(filepath):
    sent = []
    file = open(filepath, "r")
    for line in file:
        line = line.strip()
        sent.append(line)
    return sent

#tokenises
def tokenise(sent):
    tokenised_sent = {}
    tokenised_lst = []
    for line in sent:
        tokens = nltk.word_tokenize(line)
        tokenised_sent[line] = tokens
        tokenised_lst.append(tokens)
    print(tokenised_lst)
    #change to dict if want dict format
    return tokenised_lst



cornish = read_file(#input file path)
tokenised = tokenise(cornish)
