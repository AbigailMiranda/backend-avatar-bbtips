from fastapi import APIRouter, Request
from app.api.controllers.dashboard_controller import DashboardController

dashboard_router = APIRouter(
    prefix='/dashboard'
)


@dashboard_router.get('/comments_users')
def auth():
    return DashboardController().comments_users()

@dashboard_router.get('/user-parents')
def users_parents(skip: int = 0, limit: int = 10):
    return DashboardController().user_parents_info(skip, limit)

@dashboard_router.get('/question-parents')
def question_parents(skip: int = 0, limit: int = 10):
    return DashboardController().user_questions(skip, limit)