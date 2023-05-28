'''Problem model'''
from .base import CodefunABC

class Problem(CodefunABC):
    '''Represents a problem on Codefun'''
    attributes = {"id": "id", "code": "code", "name": "name"}
