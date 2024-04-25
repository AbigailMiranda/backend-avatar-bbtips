from fastapi import APIRouter, Request
from app.api.controllers.avatar_controller import AvatarController

avatar_router = APIRouter(
    prefix='/avatar'
)

@avatar_router.post('/question')
async def question(req: Request):
    question = await req.json()
    return AvatarController().get_response_for_question(question)

@avatar_router.post('/feedback')
async def save_feedback(req: Request):
    data = await req.json()
    return AvatarController().save_feedback(data)