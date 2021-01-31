# Binary Tree

This repository shows an example of using pytest in Eclpse, pyDev, Anaconda

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
1. Eclipse
2. pyDev (download from Eclipse -> Help -> Eclipse Market Place -> search pyDev)
3. Anaconda (create an virtual environment for project running in an isolated setting)
```

### Installing

Step 1: create an virtual environment using Anaconda

```
// create environment named my_env
$ conda create -n my_env python=3.6

// activate virtual enviroment
$ source activate my_env

// install required packages
$ conda install pytest

// check if package installed successfully
$ pytest --version
This is pytest version 5.2.1, imported from /$ANACONDA_PATH/envs/my_env/lib/python3.6/site-packages/pytest.py

// change to your project directory and start testing by executing
$ pytest
```

Step 2: create Eclipse project and change project setting

2.1: create project
go to File -> New -> pyDev project -> change interpreter to the path of virtual enviroment, e.g. /$ANACONDA_PATH/envs/my_env/lib/python3.6

2.2: specity the runner in pyDev project
go to Eclipse -> Reference -> pyDev -> pyUnit -> change test Runner to "Py.test runner" and delete parameter "--verbose 0"
apply and save

2.3 create file to test the function
Pytest will search for test_*.py or *_test.py files, imported by their test package name. From those files, collect test items:
- test prefixed test functions or methods outside of class
- test prefixed test functions or methods inside Test prefixed test classes (without an __init__ method)
Detail of naming rules, please refer to https://docs.pytest.org/en/latest/goodpractices.html#test-discovery


## Running the tests

1. running on Eclipse
all the testing will happen at /tests/, right click test_traversal.py -> Run as -> Python uni-test, all done

2. running on command window

```
// activate virtual enviroment
source activate my_env

// go to project directory
pytest test_traversal.py
```
