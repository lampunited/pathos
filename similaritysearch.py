from sentence_transformers import SentenceTransformer

# Load a free embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Fast, 384-dimension vectors

def get_embedding(text):
    return model.encode(text)

# Example usage
text = "How do I handle missing keys in Python dictionaries?"
embedding = get_embedding(text)
print(embedding.shape)  # Output: (384,)


# Example JSON data
data = [
    {
        "source": "reddit",
        "question_text": "How do I handle missing keys in Python dictionaries?",
        "answer_text": "Use defaultdict if you want automatic handling of missing keys.",
        "score": 120,
        "url": "https://reddit.com/r/python/comments/xyz789/",
        "tags": ["python", "dictionary", "defaultdict"]
    },
    {
        "source": "reddit",
        "question_text": "How do I optimize Python dictionary lookups?",
        "answer_text": "Use a set instead of a list for faster lookups in Python.",
        "score": 150,
        "url": "https://reddit.com/r/python/comments/abc123/some_post/",
        "tags": ["python", "performance", "dictionary"]
    },
    {
        "source": "stackoverflow",
        "question_text": "What is the time complexity of dictionary lookups?",
        "answer_text": "Dictionary lookups are O(1) on average due to hash tables.",
        "score": 200,
        "url": "https://stackoverflow.com/questions/123456",
        "tags": ["python", "hash table", "complexity"]
    }
]