'''Base class for all models'''

class CodefunABC:
    '''Represents an object returned by Codefun'''
    attributes = {}
    special = {}

    def __init__(self, data: dict):
        '''Boilerplate function for assigning things'''
        for name, new_name in self.attributes.items():
            if name not in data: continue
            if name in self.special:
                setattr(self, new_name, self.special[name](data[name]))
            else:
                setattr(self, new_name, data[name])
