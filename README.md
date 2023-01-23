# Crosswalk detection algorithm


## Table of Contents

+ [Introduction](#introduction)
+ [Getting Started](#getting_started)
    + [Prerequisites](#prerequisites)
+ [General Layout](#general_layout)
+ [How to run](#how_to_run)


## Introduction <a name = "introduction"></a>
This repository contains the model for the road markings project. The purpose of the project is to be able to identify road markings on a photograph, and classify them by damage. The classification is using the CROW standards, which are shown in second figure below. The figure below shows the goal of the project; Classified road markings. 

![image of all parts](./images/IMG10.png)

Currently we're only focussing on the crosswalks, nothing more.


## Getting Started <a name = "getting_started"></a>

### Prerequisites  <a name = "prerequisites"></a>

for all the Prerequisites, I would suggest downloading all the requirements.txt file with:

```ShellSession

$ pip install -r .\Mask_RCNN\requirements.txt
```

if there are any problem with finding the file you can manually go to the location.

## General Layout <a name = "general_layout"></a>

```bash
├── Detectron2-final
│   ├── input 
│   │   └── ...
│   ├── output
│   │   └── ...
│   ├── train
│   │   ├── Annotations_coco.json
│   │   ├── zebra1.jpg
│   │   └── ...
│   ├── valid
│   │   ├── Annotations_coco.json
│   │   ├── zebra1.jpg
│   │   └── ...
│   ├── classification.py
│   ├── custom_config_detectron.py
│   ├── environment.yml
│   ├── predicting.py
│   └── training.py
│
├── Harris_Corner_Detection_Test
│   ├── Harris.ipynb 
│   ├── img.jpg 
│   └── ... 
│
├── images
│   ├── img.jpg 
│   └── ... 
│
├── Mask_RCNN
│   ├── common 
│   │   ├── gason.cpp
│   │   ├── gason.h
│   │   ├── maskApi.c
│   │   └── maskApi.h
│   ├── datasets
│   │   ├── input
│   │   ├── output
│   │   ├── train
│   │   └── val
│   ├── logs (log files)
│   │   └── ... 
│   ├── mrcnn
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── model.py
│   │   ├── parallel_model.py
│   │   ├── utils.py
│   │   └── visualize.py
│   ├── PythonAPI
│   │   ├── pycocotools
│   │   │   ├── __init__.py
│   │   │   ├── _mask.c
│   │   │   ├── _mask.pyx
│   │   │   ├── coco.py
│   │   │   ├── cocoeval.py
│   │   │   └── mask.py
│   │   ├── Makefile
│   │   ├── pycocoDemo.ipynb
│   │   ├── pycocoEvalDemo.ipynb
│   │   └── setup.py
│   ├── scripts
│   ├── requirements.txt
│   ├── setup.cfg
│   └── setup.py
│
├── .gitignore
└── README.md
```

## How to run <a name = "how_to_run"></a>

if you've installed everything correctly you should be able to run the application.

**NOTE**: We expect you to run these commands in the home dir of the repo.

**EDIT**: This repo is no longer maintained. We suggest looking at the documentation of Detectron2 or Mask_RCNN for more information on how to make your own model with custom datasets.