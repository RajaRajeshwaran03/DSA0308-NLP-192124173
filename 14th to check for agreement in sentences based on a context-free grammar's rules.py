class AgreementChecker:
    def __init__(self, grammar):
        self.grammar = grammar

    def check_agreement(self, sentence):
        parse_tree = self.parse_sentence(sentence)
        if parse_tree:
            return self.check_subject_verb_agreement(parse_tree)
        else:
            return False

    def parse_sentence(self, sentence):
        words = sentence.split()
        return self.parse(words, self.grammar["start"])

    def parse(self, words, symbol):
        if isinstance(symbol, str):
            return symbol if symbol in words else None
        else:
            for production in self.grammar[symbol]:
                current_word_index = 0
                for symbol_in_production in production:
                    subtree = self.parse(words[current_word_index:], symbol_in_production)
                    if subtree is None:
                        break
                    current_word_index += len(subtree.split())
                if current_word_index == len(words):
                    return " ".join(production)
            return None

    def check_subject_verb_agreement(self, parse_tree):
        # Assuming the parse tree is in the form "S -> NP VP", where NP is the subject and VP is the verb phrase
        subject_verb = parse_tree.split(" -> ")[1].split()
        if len(subject_verb) != 2:
            return False
        subject, verb = subject_verb
        if subject in self.grammar["singular_nouns"] and verb in self.grammar["singular_verbs"]:
            return True
        elif subject in self.grammar["plural_nouns"] and verb in self.grammar["plural_verbs"]:
            return True
        else:
            return False
# Corrected grammar definition
grammar = {
    "start": ["S"],
    "S": [["NP", "VP"]],
    "NP": [["boy"], ["boys"]],
    "VP": [["runs"], ["run"]],
    "singular_nouns": ["boy"],
    "plural_nouns": ["boys"],
    "singular_verbs": ["runs"],
    "plural_verbs": ["run"]
}

agreement_checker = AgreementChecker(grammar)

# Test sentences
sentences = [
    "boy runs",
    "boy run",
    "boys run",
    "boys runs"
]

# Check agreement for each sentence
for sentence in sentences:
    agreement = agreement_checker.check_agreement(sentence)
    print(f"Agreement for '{sentence}': {'Agree' if agreement else 'Disagree'}")
