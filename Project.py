# Skeleton structure for a Project module

class Project:
    '''Example project class definition'''
    
    def __init__(self, conf):
        '''Initialize with config, also set up member vars for data and model modules'''
        self.m = None
        self.d = None
        self.config = conf

    def setup(self):
        '''Get data and model repositories and instantiate them'''
        pass
        
    def get_data(self):
        '''Download and verify data'''
        self.d.get()
        self.d.validate()

    def build_model(self):
        '''Build the model and check it'''
        self.m.build()
        self.m.check()

    def train_model(self):
        '''Train the model'''
        self.m.train()

    def load_weights(self):
        '''Load pre-trained weights'''
        pass
        
    def predict(self):
        '''Run the model on some data'''
        pass
