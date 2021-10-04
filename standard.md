# 1. Standard for Image Models and Data Repositories

## Summary

This document describes a standard for configuring data sets and processing (typically training and applying machine learning models) in a modular way. 

**Goals:** simplify the process of training standard models on image data sets.  Standardize configuration to support reuse of models and data.

**Limitation of scope: **concerns only image data for training classification, regression, object detection, and segmentation models.  (For now).  Non-image data and/or deployment/production is not covered.

**Checking script**: [https://github.com/ketil-malde/checkmodule](https://github.com/ketil-malde/checkmodule) (also ‘modules.txt’, a list of checkable repositories)

## 2. General architecture and functionality

There exists three possible component types: 1) the Data wrapper, 2) the Model, and 3) the Project.  Each component exports a Python class that provides the required interface, and optionally (but preferentially) runs code in a Docker container. 

Any **Docker** containers should be stateless, i.e. contain or store no data after they have been built.  It is recommended to name the current directory `/project` and to link it to the current directory on the host (i.e., `-v $CWD:/project`).

Configuration information should be stored in a shared dictionary, and modules are initialized by passing the configuration to the `__init__` method.

**TODO resolve:** 

* passing state/config to model (in a docker) 
* working and outputs in the current directory (?) 
* logging and checksumming 
* loading/running directly from dockerhub? 
* dealing with drivers/hw configs 
* get/test smaller test cases - check workings/overfit?
* run (predict) on infinite data (can’t store locally)
* versioning

# The Project component

A project component is a Git repository which clones one or more data components and one or more model components, and implements the process of linking them together. 

## Interface

(generally pass-thru for Data and Model?) 

split into train/validate/test 

## Required contents

# The Data component

A data component links to one or more data sources, and can download or otherwise provide access to data in appropriate formats following a standardized schema. 

## Interface (Data.py)

* `class Data`
* `__init__(config)`
* `build()` - (optionally) build the docker image
* `get()` - download, preprocess and/or reorganize data
* `validate()` - verify data integrity
        4. **Required contents **

```
README.md 
Data.py
Dockerfile
checksums.txt 

```

### Image classification and regression


```
images/ 
class_annotation.tsv 
regression_annotation.tsv 

```

### Object detection


```
images/
object_annotation.tsv 

```

### Segmentation

```
images/
instance_masks/ and/or 
semantic_masks/ 

```

# The Model component

A model component wraps a machine learning model and provides the necessary interface to use it. 

## Interface

* `build() `
* `check() `
* `get_weights() `
* `train() `
* `test() `
* `run() `

## Required contents

* `README.md`
* `Dockerfile`
* `Model.py`
* `src/`

# Modules

## Data

* cod otoliths _(class, regr)_
* DV (NMDC) _(class, obj loc)_
* DV simulation _(class, obj loc)_
* DV keypoints
* [Blue mussel drone images](https://github.com/ketil-malde/blue-mussel-drone-testdata) _(segmentation)_


## Models



* RetinaNet
* EfficientNet
* [U-Net](https://github.com/ketil-malde/Pytorch-UNet)
* Mask R-CNN
* Yolo v5

## Projects

* [UNet segmentation of blue mussel in drone images](https://github.com/ketil-malde/unet-blue-mussel-images)
