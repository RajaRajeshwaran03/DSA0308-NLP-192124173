import nltk
from nltk.stem import PorterStemmer

def porter_stemming(words):
    porter = PorterStemmer()
    stemmed_words = [porter.stem(word) for word in words]
    
    return stemmed_words

def main():
    words = ['running', 'ran', 'runs', 'runner', 'easily', 'fairly', 'quickly']
    
    stemmed_words = porter_stemming(words)

    for original, stemmed in zip(words, stemmed_words):
        print(f"{original} -> {stemmed}")

if __name__ == "__main__":
    main()
