import nltk
from nltk.tokenize import sent_tokenize

# Only needed once to download the required tokenizer
# nltk.download('punkt')

def sentence_tokenizer(text: str) -> list:
    """
    Splits the given text into a list of sentences.
    """
    sentences = sent_tokenize(text)
    return sentences

# Example
paragraph = "This is my new journey toward natural language processing. It is also known as NLP. I am excited to learn more."
sentences = sentence_tokenizer(paragraph)

print(f"\nOriginal text: {paragraph}")
print(f"\nAfter sentence tokenization: {sentences}\n")
