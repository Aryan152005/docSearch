
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

# Load the Sentence-BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Load document embeddings and FAISS index
doc_embeddings = np.load('doc_embeddings.npy')
index = faiss.IndexFlatL2(doc_embeddings.shape[1])
index.add(doc_embeddings)

# List of original documents
from documents import documents

def search(query, top_k=3):
    # Encode the query into a vector
    query_embedding = model.encode([query])

    # Search in the FAISS index for the top K results
    distances, indices = index.search(query_embedding, top_k)

    # Return the top K matching documents
    results = [documents[i] for i in indices[0]]
    return results
