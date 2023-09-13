from fastapi import FastAPI
from app.routes.user import create_user_router
from app.exception_handlers import add_exception_handlers

def create_profile_infos_and_users_content():
    profile_infos = {
    0 : {
        "short_description": "My bio description",
        "long_bio": 'This is our longer bio'
    }
    }

    users_content = {
        0 : {
            "liked_posts": [1, 2, 3, 4]  
        }
    }

    return profile_infos, users_content

def create_application() -> FastAPI:

    profile_infos, users_content = create_profile_infos_and_users_content()

    user_router = create_user_router(profile_infos, users_content)
    app = FastAPI()
    app.include_router(user_router)
    add_exception_handlers(app)

    return app

app = create_application()
