class PluralStateMachine:
    def __init__(self):
        self.states = {'singular', 'plural'}
        self.start_state = 'singular'
        self.accept_state = 'plural'
        self.transitions = {
            ('singular', 's'): 'plural',
            ('singular', 'x'): 'plural',
            ('singular', 'z'): 'plural',
            ('singular', 'ch'): 'plural',
            ('singular', 'sh'): 'plural',
            ('singular', 'y'): 'plural',
            ('plural', 's'): 'plural',
            ('plural', 'x'): 'plural',
            ('plural', 'z'): 'plural',
            ('plural', 'ch'): 'plural',
            ('plural', 'sh'): 'plural'
        }

    def transition(self, state, symbol):
        return self.transitions.get((state, symbol), None)

    def generate_plural(self, noun):
        current_state = self.start_state
        suffix = ''
        for i in range(len(noun)-1, -1, -1):
            symbol = noun[i:]
            next_state = self.transition(current_state, symbol)
            if next_state is None:
                break
            current_state = next_state
            if current_state == self.accept_state:
                suffix = symbol
        return noun + suffix

def main():
    machine = PluralStateMachine()
    
    nouns = ['cat', 'dog', 'church', 'box', 'brush', 'city', 'baby', 'toy']
    for noun in nouns:
        plural_form = machine.generate_plural(noun)
        print(f"The plural form of '{noun}' is '{plural_form}'")

if __name__ == "__main__":
    main()
