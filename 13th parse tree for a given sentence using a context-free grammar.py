class Node:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __str__(self):
        return self.label

def generate_parse_tree(sentence, grammar):
    words = sentence.split()
    return parse_sentence(words, grammar["start"], grammar)

def parse_sentence(words, symbol, grammar):
    if isinstance(symbol, str):
        return Node(symbol, [Node(word) for word in words]) if symbol == words[0] else None
    else:
        for production in grammar[symbol]:
            current_children = []
            current_word_index = 0
            for symbol_in_production in production:
                subtree = parse_sentence(words[current_word_index:], symbol_in_production, grammar)
                if subtree is None:
                    break
                current_children.append(subtree)
                current_word_index += count_words(subtree)
            if current_word_index == len(words):
                return Node(symbol, current_children)
        return None

def count_words(tree):
    if tree is None:
        return 0
    count = len(tree.children)
    for child in tree.children:
        count += count_words(child)
    return count

# Example usage
grammar = {
    "start": ["S"],
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"], ["N"]],
    "VP": [["V", "NP"]],
    "Det": ["the"],
    "N": ["cat", "dog"],
    "V": ["chased"]
}

sentence = "the cat chased the dog"
parse_tree = generate_parse_tree(sentence, grammar)
if parse_tree:
    print("Parse tree for the sentence:", sentence)
    print(parse_tree)
else:
    print("Failed to generate a parse tree for the sentence:", sentence)
