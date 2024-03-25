import nltk
nltk.download('averaged_perceptron_tagger')

# Download the punkt tokenizer (if not already downloaded)
nltk.download('punkt')

# Sample text
text = "Artificial intelligence is rapidly transforming the world."

# Tokenize the text (split into words)
tokens = nltk.word_tokenize(text)

# Perform part-of-speech tagging
pos_tags = nltk.pos_tag(tokens)

# Print the results
print("Original Text:", text)
print("POS Tags:", pos_tags)

# Example: Accessing individual tags
print("Part of speech for 'intelligence':", pos_tags[2][1])
