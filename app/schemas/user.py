
from pydantic import BaseModel, Field
from typing import Optional

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

class MultipleUsersResponse(BaseModel):
    users : list[FullUserProfile]

class CreateUserResponse(BaseModel):
    user_id : int
