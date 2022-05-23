# Frunch_Infinity

## Project attendees
- Kainz Fabian
- Mayr Niklas
- Mitic Dalibor

## Documentation
[Gitlab Pages](https://dalibor.mitic.pages.web.fh-kufstein.ac.at/se2_project/src)

## Goal

The goal of the project: Frunch_Infinity is, to develope an Auto-ML application with interfaces for time-series-tasks. By using this app a Non-Data Scientist can select a dataset that contains time-series via the app and compare the output of different models. Therefore, the user can get first insights if the data which has been used is usable or not. The vision of this project is to falsify the No Free Lunch Theorem.


## Brainstorm

- data set: Turbofan 
- set-up a pipeline (at the beginning start with 2 steps (e.g. scaling, delete NaN) -> incl. CI/CD
- PyCaret could be used, as it has 17 different algorithms that it is using 
- Data set should be selected via the application 
- set-up an interface between PyCaret-Output and the application 
- streamlit, plotlydash should be used for the application 

## Requirements
- Functional:
  - The frunch_infinity application must be compatible with the turbofan dataset.
  - If the user is starting app, the app has to show a list of available data sets from the ./data folder of the repository.
  - When the user is running the free lunch function via the app, the pipeline must preprocess the selected data prior to the traning of the modell.
  - When the pipeline gets data, it has to remove all missing values.
  - When the pipeline gets data, it has to scale the data.
  - When the data finishes the preprocessing via the pipeline, different models should be used to be trained for later comparison of the models.

- Technological

- Quality of Service


- User Interface:
  - If the user starts the app, they have to be able to select a data set from an available list.
  - When the models finish the training a summary table must be created showing all results of the models.
  - When the user is starting the free lunch function and any errors occur from the code, those erros should be displayed via the app to the user for debugging. 

- Requirements related to other results

- Requirements for activities


## Reflection stage 1
In stage 1 the requirements have been defined for this project using the SOPHISten rules. Based on the requirements the development of following work packages has started:
- dev-container has been created
- pipeline for preprocessing of the data based on the turbofan dataset 
  - pipeline selects a sensor as output and performs preprocessing on the input features
- CI/CD pipeline has been created
- unit tests have been created for the pipeline testing
- web-app / UI via streamlit started and postponed for stage 2
- model development has been started using pycaret 

During our first sprint, we worked on several topics at the same time. At the beginning of the project, the team had to form and agree an the same project outcome and requirements. It helped us to focus on smaller requirements first an move on to more complicated requirements later on. Step-by-step requirements were added and and will be added throughout the process. Retrospectively, it can be argued that we startet working on our code base a little bit too early. Not all requirements were completely clear and the interfaces between different parts of the software were still to be discussed.
After defining the project scope and outcome, we startet with our development setup. Meanwhile, we also implemented our first requirements. This act of balance was extremely difficult, because a consistent and working setup is the foundation of an efficient implementation. Out team was not always completely consistent with development practices and so ist happend that working on different branches and merging resulted in conflicts that had to be resolved. Especially different versions of the same packages were difficult to handle.
Also, our CI/CD Pipeline was not ready at the implementation. Therefore, our first requirements were implemented and validated a little bit later, when our pipeline was ready. A well-definied setup would have helped us during this stage. Coding standards, and defined interfaces are additional learnings from this stage. A topic that still needs a little bit focus and discussion is refactoring and the updating of our CI/CD pipeline. When creating a new feature branch the pipeline and tests should already be in place. Otherwise, validation of development only happens at the final merge which makes refactoring and improving the code more difficult. We therefore argue that moving forward the developer implementing a feature is also resposible for implementing the tests and pipeline.
Working together in person or sync the progress in online meetings is really benefitial for the overall progress. It helped ou team to refocus, improve our code and refine our requirements. Having daily standups in agile development enviroments makes sense, yet, besides working full time, it is not possible for our team to connect on a daily basis. Having a common understanding of objectives and the code is the key to project success and good software is the result of good teamwork - everyone writes their own code and how to write an "if" statement can be googled but how to work in a team is best learned by doing. We are happy with our progress in sprint 1 and know what to focus on in sprint 2.


## Tools used in this project
* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f)
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://towardsdatascience.com/introduction-to-hydra-cc-a-powerful-framework-to-configure-your-data-science-projects-ed65713a53c6)
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting  - [article](https://towardsdatascience.com/4-pre-commit-plugins-to-automate-code-reviewing-and-formatting-in-python-c80c6d2e9f5?sk=2388804fb174d667ee5b680be22b8b1f)
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project

## Sprint 1 Backlog

![](pics/Backlog_Sprint_1.png)


## Project structure
```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   ├── raw                         # raw data
│   └── raw.dvc                     # DVC file of data/raw
├── docs                            # documentation for your project
├── dvc.yaml                        # DVC pipeline
├── .flake8                         # configuration for flake8 - a Python formatter tool
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   └── train_model.py              # train model
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```

## Set up the environment
1. Install [Poetry](https://python-poetry.org/docs/#installation)
2. Set up the environment:
```bash
make activate
make setup
```

## Install new packages
To install new PyPI packages, run:
```bash
poetry add <package-name>
```

# Auto-generate API documentation

To auto-generate API document for your project, run:

```bash
make docs
```

