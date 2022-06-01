'''A collection of Codefun API's classes'''
from typing import Dict


class APIObjects:
    '''Representing an object returned by Codefun'''
    attributes = {}
    special = {}

    def __init__(self, data: Dict):
        '''Boilerplate function for assigning things'''
        for name, new_name in self.attributes.items():
            if name in self.special:
                setattr(self, new_name, self.special[name](data[name]))
            else:
                setattr(self, new_name, data[name])


class Problem(APIObjects):
    '''Represents a problem on Codefun'''
    attributes = {"id": "id", "code": "code", "name": "name"}


class Group(APIObjects):
    '''Represents a group of user on Codefun'''
    attributes = {"id": "id", "name": "name"}


class User(APIObjects):
    '''Represents an user on Codefun'''
    attributes = {"id": "id", "username": "username", "name": "name",
                  "group": "group", "status": "status", "avatar": "avatar",
                  "score": "score", "solved": "solved", "rank": "rank",
                  "ratio": "ratio"}
    special = {"group": Group}


class TestResult(APIObjects):
    '''Represents the result of a testcase'''
    attributes = {"verdict": "verdict", "runningTime": "runningTime",
                  "message": "message"}


class JudgeResult(APIObjects):
    '''Represents the result of a judge instance on a submission'''
    attributes = {"correct": "correct", "total": "total", "tests": "tests"}

    def __init__(self, data: Dict):
        '''Init specialized since "tests" is an array '''
        tests = []
        for test in data["tests"]:
            tests.append(TestResult(test))

        data["tests"] = tests
        super().__init__(data)


class Submission(APIObjects):
    '''Represents a submission. The constructor should not be called directly due to
    difference in the json format. Make calls to child classes instead'''

    attributes = {"id": "id", "problem": "problem", "owner": "owner",
                  "language": "language", "result": "result",
                  "runningTime": "runningTime", "submitTime": "submitTime",
                  "isScored": "isScored", "score": "score", "judge": "judge"}
    special = {"problem": Problem, "owner": User, "judge": JudgeResult}


# Testing
obj = Submission({
    "id": 2458680,
    "problem": {
        "id": 128,
        "code": "P002",
        "name": "P002"
    },
    "owner": {
        "id": 20915,
        "username": "NSL22_39",
        "name": "NSL22_39",
        "group": {
                    "id": 256,
                    "name": "HSGS Code Camp 2022 (NSL)\r"
        },
        "status": "Normal",
        "avatar": "https://www.gravatar.com/avatar/d41d8cd98f00b204e9800998ecf8427e?d=https:%2F%2Fs3.amazonaws.com%2Fwll-community-production%2Fimages%2Fno-avatar.png\u0026r=r\u0026s=500",
        "score": 300,
        "solved": 3,
        "rank": 9661,
        "ratio": 0.005758157389635317
    },
    "language": "C++",
    "result": "AC",
    "runningTime": 0.005,
    "submitTime": 1653928993,
    "isScored": True,
    "score": 100,
    "judge": {
        "correct": 10,
        "total": 10,
        "tests": [
                {
                    "verdict": "AC",
                    "runningTime": 0.005,
                    "message": "Output is Correct"
                },
            {
                    "verdict": "AC",
                    "runningTime": 0.005,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.002,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.002,
                    "message": "Output is Correct"
                    },
            {
                    "verdict": "AC",
                    "runningTime": 0.004,
                    "message": "Output is Correct"
                    }
        ]
    }
})
