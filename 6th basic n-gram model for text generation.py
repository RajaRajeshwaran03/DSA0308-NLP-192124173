import random

# Function to create bigrams from text
def create_bigrams(text):
    words = text.split()
    bigrams = [(words[i], words[i+1]) for i in range(len(words)-1)]
    return bigrams

# Function to generate text using bigram model
def generate_text(bigrams, length=10):
    # Choose a random starting word
    current_word = random.choice([bigram[0] for bigram in bigrams])

    generated_text = [current_word]

    for _ in range(length-1):
        possible_next_words = [bigram[1] for bigram in bigrams if bigram[0] == current_word]
        if not possible_next_words:
            break
        next_word = random.choice(possible_next_words)
        generated_text.append(next_word)
        current_word = next_word

    return ' '.join(generated_text)

# Get input text from the user
text = input("Enter some text: ")

# Create bigrams from the input text
bigrams = create_bigrams(text)

# Generate text using the bigram model
generated_text = generate_text(bigrams, length=20)
print("\nGenerated Text:")
print(generated_text)
