# Skeleton structure for a Model wrapper module

class Model:
    '''Example model class definition'''
    def __init__(self, conf, mypath):
        '''Initialize with config and path'''
        self.config = conf
        self.mypath = mypath

    def build(self):
        '''Build the docker container'''
        pass

    def check(self):
        '''Check that the configuration is okay'''
        pass
    
    def train(self):
        '''Train the network'''
        pass


