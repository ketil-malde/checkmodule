#!/usr/bin/python3
# Checker script for data, models, projects

import os
import os.path
import sys

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

def check_module(mydir):
    '''Verify that the python module exists, and go to next check'''
    files = os.listdir(mydir)
    if 'README.md' not in files:
        warn(dir, 'README is missing')
    sys.path.insert(1, mydir)
    if 'Data.py' in files:
        check_data_class(mydir)
    elif 'Model.py' in files:
        check_model_class(mydir)
    elif 'Project.py' in files:
        check_project_class(mydir)
    else:
        error(mydir,'does not seem to be a component')
        print(files)
    sys.path.remove(mydir)

data_methods = ['get', 'validate']
model_methods = ['train', 'test']
project_methods = []

def check_data_class(mydir):
    '''Check properties of the Data object'''
    print('Found data component: ',mydir)
    try:
        import Data
        d = Data.Data()
    except:
        error(mydir, "couldn't instantiate Data")
        return
    ms = [m for m in data_methods if not m in dir(d)]
    if ms != []:
        error(mydir, f'missing Data methods: {ms}')

def check_model_class(mydir):
    '''Check properties of the Model object'''
    print('Found model component: ',mydir)
    try:
        import Model
        mod = Model.Model()
    except:
        error(mydir, "couldn't instantiate Model")
        return
    ms = [m for m in model_methods if m not in dir(mod)]
    if ms != []:
        error(mydir, f'missing Model methods: {ms}')

def check_project_class(mydir):
    '''Check properties of the Project object'''
    print('Found project component: ', mydir)
    try:
        import Project
        p = Project.Project()
    except:
        error(mydir, "couldn't instantiate Project")
        return
    print(dir(p))

def check_repo(repo):
    print(repo)
    global WARN
    global ERR
    W=WARN
    E=ERR
    check_module(repo)
    if W==WARN and E==ERR:
        print(f'\033[92m{repo}:\033[0m no warning or errors')

if __name__ == '__main__':

    if len(sys.argv) == 1:
        modules = []
        with open('modules.txt') as file:
            ls = file.readlines()
            repos = [line.rstrip() for line in ls]
        for repo in repos:
            dirname = os.path.basename(repo) # does this work?
            os.system(f'git clone {repo} tmp/{dirname}')
            modules.append(f'tmp/{dirname}')
    else:
        modules = sys.argv[1:]

    print(modules)
    for repo in modules:
        check_repo(repo)
        print('--------------------')

print(f'\nTotal number of warnings: {WARN}\nTotal number of errors: {ERR}')

