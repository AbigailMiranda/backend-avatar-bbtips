from fastapi import APIRouter, Request
from app.api.controllers.user_controller import UserController

user_router = APIRouter(
    prefix='/user'
)

@user_router.post('/auth')
async def auth(req: Request):
    data = await req.json()
    return UserController().authentication(data)

@user_router.post('/validate_access_token')
async def validate(req: Request):
    data = await req.json()
    return UserController().validate_access_token(data)

@user_router.post('/send-form')
async def send_form(req: Request):
    data = await req.json()
    return UserController().get_data_user_form(data)

@user_router.post('/validate_id')
async def validate_id(req: Request):
    data = await req.json()
    return UserController().validate_id_user(data)

@user_router.post('/accept-privacity')
async def accept_privacity(req: Request):
    data= await req.json()
    return UserController().user_accept_privacity(data)