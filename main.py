from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from typing import Union, Optional
from pydantic import BaseModel, Field

app = FastAPI()


class User(BaseModel):
    username: str = Field(
        alias = "name",
        title = "The Username",
        description= "This is the username of the user",
        default = None
        )
    liked_posts: Optional[list[int]] = Field(
        description = "Array of posts ids the user liked"
    )

    class Config:
        str_max_length = 50

class FullUserProfile(User):
    short_description: str
    long_bio: str

def get_user_info(user_id : str = "default") -> FullUserProfile:
    profile_infos = {
        "default" : {
            "short_description": "My bio description",
            "long_bio": 'This is our longer bio'
        },
        "user_1" : {
            "short_description": "My bio description",
            "long_bio": 'This is our longer bio'
        }
    }
    
    user_contents = {
        "default" : {
            "username": "testuser",
            "liked_posts": [1, 2, 3]  # Example liked posts
        },
        "user_1" : {
            "username": "testuser",
            "liked_posts": [1, 2, 3]  # Example liked posts
        }
    }
    
    profile_info = profile_infos[user_id]
    user_content = user_contents[user_id]
    full_user_profile = {
        **profile_info,
        **user_content
    }
    
    return FullUserProfile(**full_user_profile)

@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id : str):

    full_user_profile = get_user_info(user_id=user_id)

    return full_user_profile

@app.get("/",  response_class=  PlainTextResponse)
def home():
    return "Welcome"
