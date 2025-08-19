import spacy
import nltk
from nltk.tag import hmm
from nltk.tokenize import word_tokenize



# Load the pre-trained spaCy model
nlp = spacy.load("en_core_web_sm")

# Custom training sentences (raw sentences, no tags)
train_sentences = train_sentences = [
    "Nitish love campusx",  # Original sentence
    "Can Nitish google campusx",  # Original sentence
    "Will ankita google campusx",  # Original sentence
    "Ankita loves Will",  # Original sentence
    "Will loves google",  # Original sentence
    "Nitish runs fast",  # Introducing a verb and an adverb
    "Ankita can sing",  # Introducing a verb and a modal
    "Will will run fast",  # Repeated word, modal and verb
    "Can Ankita read books",  # Modal verb and noun phrase
    "Nitish is a teacher",  # Copula verb 'is' and noun
    "Will google search campusx",  # Simple verb phrase with noun
    "She loves programming",  # Pronoun and verb
    "Ankita teaches math",  # Verb and noun
    "They are learning Python",  # Auxiliary verb and present continuous
    "I will eat pizza",  # First person pronoun and verb
    "The cat runs swiftly",  # Article, noun, and adverb
    "Can you help me?",  # Modal verb with pronoun
    "John plays football",  # Proper noun, verb, noun
    "The weather is great today",  # Article, noun, verb, adjective
    "I will go to the market",  # First person and future tense verb
    "The dog barks loudly",  # Article, noun, verb, adverb
    "He eats an apple every day",  # Third-person pronoun and regular verb
    "It is raining today",  # Subject and verb (copula)
    "She can swim very well",  # Pronoun, modal, verb, adverb
    "We are planning a trip",  # First person plural, auxiliary verb
    "They don't like spicy food",  # Negation and verb
    "Where is the nearest bus stop?",  # Question structure
    "Who is coming to the party?",  # Interrogative sentence
    "This book is interesting",  # Demonstrative, noun, copula, adjective
    "I like this place",  # First-person subject, verb, object
    "The sun shines brightly",  # Article, noun, verb, adverb
    "She dances beautifully",  # Pronoun, verb, adverb
    "He works in an office",  # Third-person subject, verb, preposition, article
    "They are eating pizza",  # Plural subject, verb, noun
    "This is my favorite song",  # Demonstrative, verb, possessive, noun
    "My brother is studying chemistry",  # Possessive, noun, copula, verb, noun
    "She helped me with the project",  # Pronoun, verb, object, prepositional phrase
    "They will visit Paris next summer",  # Future tense verb with noun phrase
    "Can you speak French?",  # Modal verb with noun phrase
    "I enjoy reading books",  # First-person subject, verb, gerund
    "The teacher explained the lesson",  # Article, noun, verb, object
    "We should take a break",  # Modal verb, verb, noun
    "John saw a movie last night",  # Proper noun, verb, article, noun
    "They walked to the park",  # Plural subject, verb, preposition, article, noun
    "It looks like rain",  # Subject, verb, preposition, noun
    "He is playing soccer",  # Third-person subject, verb (progressive)
    "She eats dinner at 7 PM",  # Pronoun, verb, noun phrase
    "I enjoy traveling",  # First-person subject, verb, gerund
    "They visited the museum yesterday",  # Plural subject, verb, article, noun, adverb
    "She studies mathematics at university",  # Pronoun, verb, noun, preposition
    "The kids are watching TV",  # Plural noun, auxiliary verb, noun
    "We went on a trip last weekend",  # Pronoun, verb, preposition, article, noun
    "The children are playing outside",  # Article, noun, verb, preposition
    "I have been to New York",  # First-person subject, verb (perfect)
    "She ran to the store",  # Pronoun, verb, preposition, article, noun
]


# Step 1: Tokenize and auto POS tag the sentences using spaCy
tagged_sentences = []

for sentence in train_sentences:
    doc = nlp(sentence)
    tagged_sentence = [(token.text, token.pos_) for token in doc]  # Convert to [(word, POS_tag)]
    tagged_sentences.append(tagged_sentence)

# Step 2: Train HMM model with the tagged sentences from spaCy
trainer = hmm.HiddenMarkovModelTrainer()
hmm_model = trainer.train(tagged_sentences)

# Step 3: Test the model with a new sentence
test_sentence = "Will will google campusx".split()  # Tokenize test sentence

# Step 4: Predict POS tags for the test sentence
predicted_tags = hmm_model.tag(test_sentence)

# Output the sentence and the predicted tags
print("Sentence:", test_sentence)
print("Predicted POS tags:", predicted_tags)





