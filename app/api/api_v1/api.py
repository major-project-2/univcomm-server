from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, posts, questions, comments, answers

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(posts.router, prefix='/posts', tags=['posts'])
api_router.include_router(
    comments.router, prefix='/posts/{post_id}/comments', tags=['comments'])
api_router.include_router(questions.router, prefix='/questions', tags=['questions'])
api_router.include_router(
    answers.router, prefix='/questions/{question_id}/answers', tags=['answers'])
