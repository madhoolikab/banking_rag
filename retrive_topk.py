# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 11:03:44 2024

@author: Madhu
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
import json

def get_query_embedding(query: str) -> list[float]:
    # Load embedding model
    model = TextEmbeddingModel.from_pretrained("text-embedding-005")
    task = "RETRIEVAL_DOCUMENT"
    input = TextEmbeddingInput(query, task)
    dimensionality = 256
    kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
    embedding = model.get_embeddings([input], **kwargs)[0]
    return embedding.values

def retrieve_relevant_chunks(query: str, chunks_file: str, top_k: int = 3):
    # Load chunks with embeddings
    with open(chunks_file, "r") as file:
        chunks = json.load(file)

    # Extract embeddings and compute cosine similarity
    embeddings = np.array([chunk["embedding"] for chunk in chunks])
    query_embedding = np.array(get_query_embedding(query)).reshape(1, -1)
    similarities = cosine_similarity(query_embedding, embeddings).flatten()

    # Retrieve top-k chunks
    top_indices = np.argsort(similarities)[-top_k:][::-1]
    top_chunks = [chunks[i] for i in top_indices]

    return top_chunks

# Example usage
query = "What are the eligibility criteria for opening an account?"
top_chunks = retrieve_relevant_chunks(query, "chunks_with_embeddings.json", top_k=3)

# Print relevant chunks
for i, chunk in enumerate(top_chunks, 1):
    print(f"Top {i}: {chunk['text']}")
