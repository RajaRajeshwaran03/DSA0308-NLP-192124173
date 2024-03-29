import nltk
from nltk.corpus import wordnet

# Function to extract noun phrases and their meanings
def extract_noun_phrases(sentence):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(sentence)

    # Perform part-of-speech tagging
    tagged_words = nltk.pos_tag(words)

    # Extract noun phrases
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    cp = nltk.RegexpParser(grammar)
    tree = cp.parse(tagged_words)

    noun_phrases = []
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            # Extract noun phrase
            noun_phrase = " ".join(word for word, tag in subtree.leaves())
            noun_phrases.append(noun_phrase)

            # Get meanings of the noun phrase
            meanings = []
            for word, tag in subtree.leaves():
                synsets = wordnet.synsets(word)
                for synset in synsets:
                    meanings.append(f"{synset.name()}: {synset.definition()}")
            print(f"Noun Phrase: {noun_phrase}, Meanings: {meanings}")

    return noun_phrases

# Get input from user
sentence = input("Enter a sentence: ")

# Extract noun phrases and their meanings
noun_phrases = extract_noun_phrases(sentence)
