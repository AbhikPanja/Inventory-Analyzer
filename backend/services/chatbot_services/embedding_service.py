import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from services.chatbot_services.chunk_service import (get_inventory_chunks)

load_dotenv()

MODEL_NAME = os.getenv("EMBEDDING_MODEL")

embedding_model = SentenceTransformer(MODEL_NAME)


def embed_text(text):

    embedding = embedding_model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding

def embed_chunks(chunks):

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


def get_inventory_embeddings():

    chunks = get_inventory_chunks()

    embeddings = embed_chunks(chunks)

    return chunks, embeddings