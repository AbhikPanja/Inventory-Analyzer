from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from services.chatbot_services.retrieval_service import (
    get_relevant_context
)

from services.chatbot_services.llm_service import (
    generate_response
)

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/")
def chat(request: ChatRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:
        context = get_relevant_context(question)
        

        answer = generate_response(
            question,
            context
        )

        return {
            "question": question,
            "answer": answer
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
    