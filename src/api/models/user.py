'''Models related to a user'''
from .base import CodefunABC

class Group(CodefunABC):
    '''Represents a group of user on Codefun'''
    attributes = {"id": "id", "name": "name"}


class User(CodefunABC):
    '''Represents an user on Codefun'''
    attributes = {"id": "id", "username": "username", "name": "name",
                  "group": "group", "status": "status", "avatar": "avatar",
                  "score": "score", "solved": "solved", "rank": "rank",
                  "ratio": "ratio"}
    special = {"group": Group}
