import os
import pickle
import faiss
import numpy as np
from services.chatbot_services.embedding_service import (get_inventory_embeddings)

_index = None
_chunks = None


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

VECTOR_STORE = os.path.join(
    BASE_DIR,
    "vector_store"
)

os.makedirs(VECTOR_STORE, exist_ok=True)

INDEX_PATH = os.path.join(
    VECTOR_STORE,
    "inventory.index"
)

CHUNK_PATH = os.path.join(
    VECTOR_STORE,
    "chunk_store.pkl"
)


def build_vector_store():
    chunks, embeddings = get_inventory_embeddings()
    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    faiss.write_index(
        index,
        INDEX_PATH
    )
    with open(CHUNK_PATH, "wb") as f:
        pickle.dump(chunks, f)
    # Clear cache so the next search loads the updated vector store
    global _index, _chunks
    _index = None
    _chunks = None
    
    print(
        f"Indexed {len(chunks)} inventory records."
    )


def load_vector_store():
    global _index, _chunks

    # Return cached index and chunks if already loaded
    if _index is not None and _chunks is not None:
        return _index, _chunks

    # Check if files exist
    if not os.path.exists(INDEX_PATH):
        raise FileNotFoundError(
            "Vector index not found."
        )

    if not os.path.exists(CHUNK_PATH):
        raise FileNotFoundError(
            "Chunk store not found."
        )

    # Load from disk
    _index = faiss.read_index(INDEX_PATH)

    with open(CHUNK_PATH, "rb") as f:
        _chunks = pickle.load(f)

    return _index, _chunks


def search_vectors(
    query_embedding,
    top_k=8
):

    index, chunks = load_vector_store()

    query_embedding = np.array(
        [query_embedding],
        dtype=np.float32
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for idx in indices[0]:
        results.append(chunks[idx])

    return results