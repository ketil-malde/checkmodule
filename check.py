# Checker script for data, models, projects

import os
import os.path

ERR=0
WARN=0

def warn(dir, str):
    global WARN
    print('\033[93mWARNING: '+dir+': \033[0m'+str)
    WARN+=1

def error(dir, str):
    global ERR
    print('\033[91mERROR: '+dir+': \033[0m'+str)
    ERR+=1

import sys

def check_module(dir):
    '''Verify that the python module exists, and go to next check'''
    files = os.listdir(dir)
    if 'README.md' not in files:
        warn(dir, 'README is missing')
    sys.path.insert(1, dir)
    if 'Data.py' in files:
        check_data_class(dir)
    elif 'Model.py' in files:
        check_model_class(dir)
    elif 'Project.py' in files:
        check_project_class(dir)
    else:
        error(dir,'does not seem to be a component')
        print(files)
    sys.path.remove(dir)

def check_data_class(dir):
    '''Check properties of the Data object'''
    print('Found data component: ',dir)
    import Data
    d = Data.Data()
    print(dir(d))
    #check that d has get() and validate()

def check_model_class(dir):
    '''Check properties of the Model object'''
    print('Found model component: ',dir)
    import Model
    m = Model.Model()
    print(dir(m))

def check_project_class(dir):
    '''Check properties of the Project object'''
    print('Found project component: ', dir)
    import Project
    p = Project.Project()
    print(dir(p))

# something something __main__

modules = [
    '--branch standardize https://github.com/ketil-malde/maskrcnn-docker',
    'git@git.imr.no:endrem/imr_ml_datastore.git'
    ]

def check_repo(repo):
    global WARN
    global ERR
    W=WARN
    E=ERR
    dirname = os.path.basename(repo) # does this work?
    os.system(f'git clone {repo} tmp/{dirname}')
    check_module('tmp/'+dirname)
    if W==WARN and E==ERR:
        print(f'\033[92m{dirname}:\033[0m no warning or errors')

for repo in modules:
    check_repo(repo)
    print('--------------------')

print(f'\nTotal number of warnings: {WARN}\nTotal number of errors: {ERR}')

