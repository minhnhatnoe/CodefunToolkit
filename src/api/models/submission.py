'''Models related to a submission'''
from dateutil import tz
from datetime import datetime
from .base import CodefunABC
from .problem import Problem
from .user import User

class TestResult(CodefunABC):
    '''Represents the result of a testcase'''
    attributes = {"verdict": "verdict", "runningTime": "runningTime",
                  "message": "message"}


class JudgeResult(CodefunABC):
    '''Represents the result of a judge instance on a submission'''
    attributes = {"correct": "correct", "total": "total", "tests": "tests"}

    def __init__(self, data: dict):
        '''Init specialized since "tests" is an array '''
        tests = []
        for test in data["tests"]:
            tests.append(TestResult(test))

        data["tests"] = tests
        super().__init__(data)


class Submission(CodefunABC):
    '''Represents a submission. The constructor should not be called directly due to
    difference in the json format. Make calls to child classes instead'''

    attributes = {"id": "id", "problem": "problem", "owner": "owner",
                  "language": "language", "result": "result",
                  "runningTime": "runningTime", "submitTime": "submitTime",
                  "isScored": "isScored", "score": "score", "judge": "judge"}
    special = {"problem": Problem, "owner": User, "judge": JudgeResult}
    
    @property
    def submit_timestamp(self):
        timezone = tz.tzstr("GMT+7")
        return datetime.fromtimestamp(self.submitTime, tz=timezone)

    @property
    def submit_timestamp_notz(self):
        return datetime.fromtimestamp(self.submitTime)