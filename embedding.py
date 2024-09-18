
from sentence_transformers import SentenceTransformer

# Load pre-trained Sentence-BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Import your document dataset
from documents import documents

# Encode the documents into embeddings
doc_embeddings = model.encode(documents)

# Save the embeddings for later use
import numpy as np
np.save('doc_embeddings.npy', doc_embeddings)
