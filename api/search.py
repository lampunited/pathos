import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load FAISS index and ID map
index = faiss.read_index("api/index/faiss_index.bin")
id_map = np.load("api/index/id_map.npy", allow_pickle=True).item()

def search_faiss(query, top_k=3):
    """Search FAISS for similar results given a query."""
    query_embedding = model.encode([query]).astype('float32')
    
    distances, indices = index.search(query_embedding, top_k)  # Search top K similar items
    
    results = []
    for i, idx in enumerate(indices[0]):  # Loop through results
        if idx != -1:
            result = id_map[idx]
            result["distance"] = float(distances[0][i])  # Add similarity score
            results.append(result)
    
    return results

if __name__ == "__main__":
    # Example Query
    query = "Can you help me login to github"
    results = search_faiss(query, top_k=10)

    # Print results
    for res in results:
        #print(f"Question: {res['question_text']}")
        print(f"Answer: {res['answer_text']}")
        print(f"Distance: {res['distance']:.4f}")
        #print(f"URL: {res['url']}\n")
