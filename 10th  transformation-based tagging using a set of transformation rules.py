import random

# Sample training data
training_corpus = [
    ("The", "DET"),
    ("quick", "ADJ"),
    ("brown", "ADJ"),
    ("fox", "NOUN"),
    ("jumps", "VERB"),
    ("over", "ADP"),
    ("the", "DET"),
    ("lazy", "ADJ"),
    ("dog", "NOUN")
]

# Transition probabilities
transition_probabilities = {
    "DET": {"NOUN": 0.6, "ADJ": 0.3, "VERB": 0.1},
    "ADJ": {"NOUN": 0.5, "DET": 0.4, "ADP": 0.1},
    "NOUN": {"VERB": 0.4, "ADP": 0.4, "DET": 0.2},
    "VERB": {"ADP": 0.6, "DET": 0.2, "NOUN": 0.2},
    "ADP": {"DET": 0.6, "NOUN": 0.2, "VERB": 0.2}
}

# Simple stochastic part-of-speech tagging function
def stochastic_pos_tagging(sentence):
    tagged_sentence = []
    previous_tag = None

    for word in sentence:
        if previous_tag is None:
            # Start with a random POS tag for the first word
            tag = random.choice(list(transition_probabilities.keys()))
        else:
            # Choose the next POS tag based on transition probabilities
            tag = random.choices(list(transition_probabilities[previous_tag].keys()),
                                 weights=transition_probabilities[previous_tag].values())[0]

        tagged_sentence.append((word, tag))
        previous_tag = tag

    return tagged_sentence

# Example usage
sentence = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
tagged_sentence = stochastic_pos_tagging(sentence)
print(tagged_sentence)
