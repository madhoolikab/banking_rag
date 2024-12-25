# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 06:38:21 2024

@author: Madhu
"""

from __future__ import annotations

import json
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

def embed_text() -> list[list[float]]:
    """Embeds texts with a pre-trained, foundational model.

    Returns:
        A list of lists containing the embedding vectors for each input text
    """

    # A list of texts to be embedded.
    texts = ["banana muffins? ", "banana bread? banana muffins?"]
    dimensionality = 256
    task = "RETRIEVAL_DOCUMENT"

    model = TextEmbeddingModel.from_pretrained("text-embedding-005")
    inputs = [TextEmbeddingInput(text, task) for text in texts]
    kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
    embeddings = model.get_embeddings(inputs, **kwargs)

    return [embedding.values for embedding in embeddings]



def embed_chunks(input_file: str, output_file: str):
    # Load chunks from JSON
    with open(input_file, "r") as file:
        chunks = json.load(file)

    # Extract texts to embed
    texts = [chunk["text"] for chunk in chunks]
    task = "RETRIEVAL_DOCUMENT"

    # Load the embedding model
    model = TextEmbeddingModel.from_pretrained("text-embedding-005")
    inputs = [TextEmbeddingInput(text, task) for text in texts]

    # Generate embeddings
    dimensionality = 256
    kwargs = dict(output_dimensionality=dimensionality) if dimensionality else {}
    embeddings = model.get_embeddings(inputs, **kwargs)

    # Add embeddings to chunks
    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding.values

    # Save updated chunks to output JSON
    with open(output_file, "w") as file:
        json.dump(chunks, file, indent=4)

# Run the embedding process
embed_chunks("chunks.json", "chunks_with_embeddings.json")
