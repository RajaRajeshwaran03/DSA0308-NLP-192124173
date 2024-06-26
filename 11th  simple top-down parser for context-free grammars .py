class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.input_string = input_string
        self.index = 0
        try:
            self.parse_expression(self.grammar["start"])
            if self.index == len(input_string):
                print("Parsing Successful!")
            else:
                print("Parsing Failed: Input not fully consumed.")
        except Exception as e:
            print("Parsing Failed:", e)

    def parse_expression(self, expression):
        print("Parsing expression:", expression)
        for element in expression:
            if element in self.grammar:
                self.parse_expression(self.grammar[element])
            else:
                self.match_terminal(element)

    def match_terminal(self, terminal):
        print("Matching terminal:", terminal)
        if self.index < len(self.input_string) and self.input_string[self.index] == terminal:
            print("Matched terminal:", terminal)
            self.index += 1
        else:
            raise Exception(f"Expected '{terminal}' but found '{self.input_string[self.index]}'")


# Grammar
grammar = {
    "start": ["expr"],
    "expr": ["term", "+", "expr"],
    "term": ["factor"],
    "factor": ["(", "expr", ")", "number"],
    "number": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
}

# Main program
parser = Parser(grammar)
input_string = input("Enter input string: ")
parser.parse(input_string)
