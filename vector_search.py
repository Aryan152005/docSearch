
import faiss
import numpy as np

# Load document embeddings
doc_embeddings = np.load('doc_embeddings.npy')

# Create a FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)  # L2 distance index
index.add(doc_embeddings)  # Add document embeddings to the index
