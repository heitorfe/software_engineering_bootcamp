class UserNotFound(Exception):
    def __init__(self, user_id) -> None:
        self.user_id = user_id