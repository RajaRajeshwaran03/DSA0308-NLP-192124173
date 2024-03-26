class State:
    def __init__(self, rule, dot_position, start_position):
        self.rule = rule
        self.dot_position = dot_position
        self.start_position = start_position

    def __eq__(self, other):
        return self.rule == other.rule and self.dot_position == other.dot_position and self.start_position == other.start_position

    def __hash__(self):
        return hash((self.rule, self.dot_position, self.start_position))

    def __str__(self):
        rule = self.rule.split(" -> ")[0]
        expansion = " ".join(self.rule.split(" -> ")[1])
        return f"{rule} -> {' '.join(expansion[:self.dot_position])} * {' '.join(expansion[self.dot_position:])} [{self.start_position}]"


class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.chart = []

    def predict(self, state):
        next_symbol = state.rule.split(" -> ")[1][state.dot_position]
        for rule in self.grammar:
            if rule.startswith(next_symbol):
                new_state = State(rule, 0, state.start_position)
                if new_state not in self.chart[state.start_position]:
                    self.chart[state.start_position].append(new_state)

    def scan(self, state, token):
        next_symbol = state.rule.split(" -> ")[1][state.dot_position]
        if token == next_symbol:
            new_state = State(state.rule, state.dot_position + 1, state.start_position)
            if new_state not in self.chart[state.start_position + 1]:
                self.chart[state.start_position + 1].append(new_state)

    def complete(self, state):
        for s in self.chart[state.start_position]:
            if s.dot_position < len(s.rule.split(" -> ")[1]) and s.rule.split(" -> ")[1][s.dot_position] == state.rule.split(" -> ")[0]:
                new_state = State(s.rule, s.dot_position + 1, s.start_position)
                if new_state not in self.chart[state.start_position]:
                    self.chart[state.start_position].append(new_state)

    def parse(self, input_string):
        self.chart = [[] for _ in range(len(input_string) + 1)]
        start_state = State("start -> S", 0, 0)
        self.chart[0].append(start_state)

        for i in range(len(input_string) + 1):
            for state in self.chart[i]:
                if state.dot_position < len(state.rule.split(" -> ")[1]):
                    self.predict(state)
                else:
                    self.complete(state)
                if i < len(input_string):
                    self.scan(state, input_string[i])
            
            print(f"Chart[{i}]:")
            for state in self.chart[i]:
                print(state)

        if State("start -> S", 1, 0) in self.chart[len(input_string)]:
            print("Parsing Successful!")
        else:
            print("Parsing Failed!")


# Grammar
grammar = [
    "start -> S",
    "S -> NP VP",
    "NP -> Det N",
    "VP -> V NP",
    "Det -> 'the'",
    "N -> 'cat'",
    "N -> 'dog'",
    "V -> 'chased'"
]

# Main program
parser = EarleyParser(grammar)
input_string = input("Enter input string: ").split()
parser.parse(input_string)
