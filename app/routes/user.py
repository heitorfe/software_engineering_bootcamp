from fastapi import  APIRouter, HTTPException, Depends
from app.schemas.user import (
    FullUserProfile,
    MultipleUsersResponse,
    CreateUserResponse,
)
from app.services.user import UserService
from app.dependenceis import rate_limit
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(
    format =  '%(levelname)-6s %(name)-15s %(asctime)s.%(msecs)03d %(message)s',
    datefmt= "%y-%m-%d %H:%M:%S",
    filename = "log.txt",
    )
logger.setLevel(logging.INFO)

console = logging.StreamHandler()
logger.addHandler(console)


def create_user_router(profile_infos : dict, users_content : dict ) -> APIRouter:
    user_router = APIRouter(
        prefix = "/user",
        tags = ["user"],
        dependencies= [Depends(rate_limit)])
    
    user_service = UserService(profile_infos, users_content)

    @user_router.get("/{user_id}", response_model=FullUserProfile)
    async def get_user_by_id(user_id : int):
        """
        Endpoint for retrieving a FullUserProfile by the user's unique integer id

        :param user_id: int - unique monotonically increasing integer id
        :return: FullUserProfile
        """
        try:
            full_user_profile = await user_service.get_user_info(user_id)

        except KeyError:
            logger.error(f"Non-existent user_id : {user_id} was requested")
            raise HTTPException(status_code=404, detail="User doesn't exist")
        return full_user_profile

    @user_router.put("/{user_id}")
    async def update_user(user_id: int, full_profile_info : FullUserProfile):
        await user_service.create_update_user(full_profile_info, user_id)
        return None

    @user_router.delete("/{user_id}")
    async def remove_user(user_id: int):
        logger.info(f"About to delete user: {user_id}")
        try:
            await user_service.delete_user(user_id) 
        except KeyError:
            logger.error(f"Non-existent user_id : {user_id} was requested")
            raise HTTPException(status_code=404, detail={"msg" : "User doesn't exist", "user_id" : user_id})

    @user_router.get("/all", response_model=MultipleUsersResponse)
    async def get_all_users_paginated(start: int = 0, limit: int = 2):
        users, total = await user_service.get_all_users_with_pagination(start=start, limit = limit)
        formatted_users = MultipleUsersResponse(users=users, total=total)
        return formatted_users

    @user_router.post("/", response_model = CreateUserResponse, status_code=201)
    async def add_user(full_profile_info : FullUserProfile):
        logger.info("alo")
        user_id =  await user_service.create_update_user(full_profile_info)
        created_user = CreateUserResponse(user_id = user_id)
        return created_user
    
    return user_router