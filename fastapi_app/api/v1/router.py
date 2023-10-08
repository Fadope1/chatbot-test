from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from ...models.input import OpenAIRequestSchema
from ...services.llm import generate_sentence

router = APIRouter()


@router.post("/ask-me")
async def ask_me(body: OpenAIRequestSchema):
    if "data" in body.prompt:
        return test_vis()

    return StreamingResponse(generate_sentence(**body.model_dump()))


def test_vis():
    return {
        "type": "line",
        "x": [1, 2, 3],
        "y": [5, 6, 4]
    }
