import nltk
from nltk.tokenize import word_tokenize

def word_tokenizer(text:str)->list:
    
    tokenize = word_tokenize(text)
    
    return tokenize
    
    

sentence  = "this is my new journey toward natural language processing also known as NLP"
tokenize = word_tokenizer(sentence)


print(f"\noriginal sentence is {sentence} ")
print(f"\nafter word tokenize : {tokenize}\n")