from textblob import TextBlob
import nltk
import textblob


# Sample text with intentional spelling mistakes
incorrect_text = "Plase corect this speling mistak. It is importent for good comunication."
print(f"Original Text with Misspellings:\n{incorrect_text}")

# Create a TextBlob object and correct the spelling
blob = TextBlob(incorrect_text)
corrected_text = str(blob.correct())

print(f"\nText After Spelling Correction (TextBlob):\n{corrected_text}")
