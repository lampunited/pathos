import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import json
from tqdm import tqdm
import os

# Load SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')


def create_index(data):
    # Generate embeddings and store them in an array
    embeddings = []
    id_map = {}

    for idx, item in tqdm(enumerate(data), desc="Creating FAISS index: ", total=len(data)):
        text_to_embed = f"{item['answer_text']}"
        #text_to_embed = f"{item['question_text']}"
        embedding = model.encode(text_to_embed)
        
        embeddings.append(embedding)
        id_map[idx] = item  # Store mapping of FAISS index to original data
        # print(id_map[idx])

    embeddings = np.array(embeddings).astype('float32')  # Convert to FAISS-compatible format

    # Initialize FAISS index
    dimension = embeddings.shape[1]  # Embedding size (384 for MiniLM)
    index = faiss.IndexFlatL2(dimension)  # L2 distance (Euclidean)

    # **Check if old index exists and delete it before saving the new one**
    if os.path.exists("api/index/faiss_index.bin"):
        os.remove("api/index/faiss_index.bin")

    if os.path.exists("api/index/id_map.npy"):
        os.remove("api/index/id_map.npy")

    # Add embeddings to FAISS index
    index.add(embeddings)

    # Save FAISS index for later use
    faiss.write_index(index, "api/index/faiss_index.bin")
    np.save("api/index/id_map.npy", id_map)  # Save ID map for retrieval

    print("FAISS index created and saved!")

if __name__ == "__main__":
    # Load JSON file
    with open("api/reddit_results.json", "r", encoding="utf-8") as f:
        data = json.load(f)  # This loads the JSON array into the variable `data`

    create_index(data)
