class FiniteStateAutomaton:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.start_state = 'q0'
        self.accept_states = {'q2'}
        self.transitions = {
            ('q0', 'a'): 'q1',
            ('q1', 'b'): 'q2'
        }

    def is_accepting(self, state):
        return state in self.accept_states

    def transition(self, state, symbol):
        return self.transitions.get((state, symbol))

    def accepts(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            next_state = self.transition(current_state, symbol)
            if next_state is None:
                return False
            current_state = next_state
        return self.is_accepting(current_state)

def main():
    automaton = FiniteStateAutomaton()
    
    test_strings = ['ab', 'aab', 'abb', 'aaaab', 'baab']
    
    for string in test_strings:
        if automaton.accepts(string):
            print(f"'{string}' is accepted")
        else:
            print(f"'{string}' is not accepted")

if __name__ == "__main__":
    main()
