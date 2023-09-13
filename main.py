from fastapi import FastAPI
from app.routes.user import create_user_router


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

def create_applitcation() -> FastAPI:

    profile_infos, users_content = create_profile_infos_and_users_content()

    user_router = create_user_router(profile_infos, users_content)
    app = FastAPI()
    app.include_router(user_router)
    return app

app = create_applitcation()
