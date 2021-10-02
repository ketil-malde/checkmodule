#!/usr/bin/python3
# Checker script for data, models, projects

import os
import os.path
import sys

ERR=0
WARN=0

def warn(mydir, mystr):
    global WARN
    print('\033[93mWARNING: '+mydir+': \033[0m'+mystr)
    WARN+=1

def error(mydir, mystr):
    global ERR
    print('\033[91mERROR: '+mydir+': \033[0m'+mystr)
    ERR+=1

def check_module(mydir):
    '''Verify that the python module exists, and go to next check'''
    files = os.listdir(mydir)
    if 'README.md' not in files:
        warn(mydir, 'README is missing')
    sys.path.insert(1, mydir)
    if 'Data.py' in files:
        check_data_class(mydir)
    elif 'Model.py' in files:
        check_model_class(mydir)
    elif 'Project.py' in files:
        check_project_class(mydir)
    else:
        error(mydir,'does not seem to be a component')
        print('files:', files)
    sys.path.remove(mydir)

data_methods = ['get', 'validate']
model_methods = ['train', 'test']
project_methods = ['get_data', 'train_model']

import logging

def check_data_class(mydir):
    '''Check properties of the Data object'''
    print('Found data component: ', mydir)
    try:
        import Data
        d = Data.Data({}, '')
    except:
        error(mydir, "couldn't instantiate Data")
        logging.excpetion("couldn't instantiate Data")
        return
    ms = [m for m in data_methods if not m in dir(d)]
    if ms != []:
        error(mydir, f'missing Data methods: {ms}')
        
def check_model_class(mydir):
    '''Check properties of the Model object'''
    print('Found model component: ',mydir)
    try:
        import Model
        mod = Model.Model({}, '')
    except:
        error(mydir, "couldn't instantiate Model")
        logging.exception("couldn't instantiate Model")        
        return
    ms = [m for m in model_methods if m not in dir(mod)]
    if ms != []:
        error(mydir, f'missing Model methods: {ms}')
        
def check_project_class(mydir):
    '''Check properties of the Project object'''
    print('Found project component: ', mydir)
    try:
        import Project
        p = Project.Project({})
    except:
        error(mydir, "couldn't instantiate Project")
        logging.exception("couldn't instantiate Model")
        return
    del Project

def check_repo(repo):
    print(repo)
    global WARN
    global ERR
    W=WARN
    E=ERR
    check_module(repo)
    if W==WARN and E==ERR:
        print(f'\033[92m{repo}:\033[0m no warnings or errors')
    else:
        print(f'\033[93m{repo}:\033[0m {WARN-W} warnings and {ERR-E} errors')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        check_repo(sys.argv[1])
    else:
        print(f'Usage {argv[0]} <repository>')


