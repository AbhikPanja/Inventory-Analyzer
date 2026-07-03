from services.chatbot_services.embedding_service import (embed_text)
from services.chatbot_services.faiss_service import (search_vectors)


def retrieve_context(question,top_k=5):
    question_embedding = embed_text(question)
    retrieved_chunks = search_vectors(
        question_embedding,
        top_k=top_k
    )
    return retrieved_chunks


def build_context(chunks):
    return "\n\n".join(chunks)


def get_relevant_context(question,top_k=5):
    chunks = retrieve_context(question,top_k)
    return build_context(chunks)