'''A collection of Codefun API's classes'''
from .problem import Problem
from .submission import TestResult, JudgeResult, Submission
from .user import Group, User

__all__ = ["Problem",
           "TestResult", "JudgeResult", "Submission",
           "Group", "User"]

# Testing
test_obj = Submission({
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
