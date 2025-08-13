import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Only needed once to download required NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

def remove_stopwords(text: str) -> list:
    """
    Removes English stopwords from the given text and returns the filtered tokens.
    """
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [i for i in words if i.lower() not in stop_words]
    return filtered_words

sentence = "This is my new journey toward natural language processing, also known as NLP."
filtered_tokens = remove_stopwords(sentence)

print(f"\nOriginal text: {sentence}")
print(f"\nAfter stopword removal: {filtered_tokens}\n")
