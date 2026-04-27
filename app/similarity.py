from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from app.model import model, inputs, embeddings


def find_best_match(query: str):
    query_embedding = model.encode([query])

    similarities = cosine_similarity(query_embedding, embeddings)[0]
    top_index = int(np.argmax(similarities))

    return {
        "query": query,
        "top_match": inputs[top_index],
        "similarity_score": float(similarities[top_index])
    }