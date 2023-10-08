from .base import BaseInputSchema


class OpenAIRequestSchema(BaseInputSchema):
    prompt: str
    system: str | None = None
    history: list[dict[str, str]] | None = None