from nltk.corpus import wordnet

def explore_word_meanings(word):
    # Retrieve synsets for the given word
    synsets = wordnet.synsets(word)
    
    if not synsets:
        print(f"No synsets found for the word '{word}'")
        return
    
    print(f"Synsets for the word '{word}':")
    for synset in synsets:
        print(f"Synset: {synset.name()}")
        print(f"Definition: {synset.definition()}")
        print(f"Examples: {synset.examples()}")
        print()

# Example word to explore
word = "car"

# Explore word meanings
explore_word_meanings(word)
