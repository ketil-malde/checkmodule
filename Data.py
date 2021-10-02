# Skeleton structure for a Data wrapper module

class Data:
    '''Example data class definition'''
    def __init__(self, conf, mypath):
        '''Initialize with config and path'''
        self.config = conf
        self.mypath = mypath

    def get(self):
        '''Download, unpack, and organize the data'''
        pass

    def validate(self):
        '''Check data completeness and integrity'''
