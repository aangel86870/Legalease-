from fastapi import APIRouter
from pydantic import BaseModel
from ai_core.gemini_generator import generate_document

router = APIRouter()


class DocumentRequest(BaseModel):
    document_type: str
    parties: str
    terms: str
    dates: str


@router.post("/generate")
def generate(request: DocumentRequest):
    document = generate_document(
        request.document_type,
        request.parties,
        request.terms,
        request.dates
    )

    return {
        "success": True,
        "document": document
      }
