from sentence_transformers import SentenceTransformer
import json

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load sample inputs
with open("data/sample_inputs.json", "r") as f:
    inputs = json.load(f)

# Precompute embeddings
embeddings = model.encode(inputs)