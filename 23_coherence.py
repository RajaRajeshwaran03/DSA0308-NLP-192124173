from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def evaluate_coherence(text):
    # Create a TF-IDF Vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the text data
    tfidf_matrix = vectorizer.fit_transform(text)
    
    # Calculate cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Average pairwise cosine similarity
    coherence_score = (cosine_sim.sum() - len(text)) / (len(text) * (len(text) - 1))
    
    return coherence_score

# Get input from the user
text = [input("Enter a sentence: ") for _ in range(5)]  # You can adjust the number of sentences for evaluation

# Evaluate the coherence of the text
coherence_score = evaluate_coherence(text)
print("Coherence Score:", coherence_score)
