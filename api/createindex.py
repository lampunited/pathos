import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Example dataset
data = [
    {
        "source": "reddit",
        "question_text": "How do I handle missing keys in Python dictionaries?",
        "answer_text": "Use defaultdict if you want automatic handling of missing keys.",
        "score": 120,
        "url": "https://reddit.com/r/python/comments/xyz789/",
    },
    {
        "source": "reddit",
        "question_text": "How do I optimize Python dictionary lookups?",
        "answer_text": "Use a set instead of a list for faster lookups in Python.",
        "score": 150,
        "url": "https://reddit.com/r/python/comments/abc123/some_post/",
    },
    {
        "source": "stackoverflow",
        "question_text": "What is the time complexity of dictionary lookups?",
        "answer_text": "Dictionary lookups are O(1) on average due to hash tables.",
        "score": 200,
        "url": "https://stackoverflow.com/questions/123456",
    }
]

def create_index(data):
    # Generate embeddings and store them in an array
    embeddings = []
    id_map = {}

    for idx, item in enumerate(data):
        text_to_embed = f"{item['question_text']} {item['answer_text']}"
        embedding = model.encode(text_to_embed)
        
        embeddings.append(embedding)
        id_map[idx] = item  # Store mapping of FAISS index to original data

    embeddings = np.array(embeddings).astype('float32')  # Convert to FAISS-compatible format

    # Initialize FAISS index
    dimension = embeddings.shape[1]  # Embedding size (384 for MiniLM)
    index = faiss.IndexFlatL2(dimension)  # L2 distance (Euclidean)

    # Add embeddings to FAISS index
    index.add(embeddings)

    # Save FAISS index for later use
    faiss.write_index(index, "index/faiss_index.bin")
    np.save("index/id_map.npy", id_map)  # Save ID map for retrieval

    print("FAISS index created and saved!")

create_index(data)
