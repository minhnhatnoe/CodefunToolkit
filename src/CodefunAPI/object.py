from typing import Dict


class APIObjects:
    attributes = {}
    special = {}

    def __init__(self, data: Dict):
        for name, new_name in self.attributes.items():
            if name in self.special:
                self.new_name = self.special[name](data[name])
            else:
                self.new_name = data[name]


class Problem(APIObjects):
    attributes = {"id": "id", "code": "code", "name": "name"}


class Group(APIObjects):
    attributes = {"id": "id", "name": "name"}


class User(APIObjects):
    attributes = {"id": "id", "username": "username", "name": "name",
                  "group": "group", "status": "status", "avatar": "avatar",
                  "score": "score", "solved": "solved", "rank": "rank",
                  "ratio": "ratio"}
    special = {"group": Group}


class Submission(APIObjects):
    attributes = ["id", "problem", "owner", "language", "result",
                  "runningTime", "submitTime", "isScored", "score"]
    special = {"problem": Problem, "owner": User}

    def init(self, data: Dict, source: int):
        '''If source is 1, then data comes from profile page.
        Else if source is 2, then data comes from submissions page'''
        if source == 1:
            pass
