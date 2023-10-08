from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ...models.input import OpenAIRequestSchema
from ...services.llm import generate_sentence

router = APIRouter()


@router.post("/ask-me")
async def ask_me(body: OpenAIRequestSchema):
    return StreamingResponse(generate_sentence(body.prompt))
