# UNICEF-AI-Personalisation
Some children learn best by watching videos, some by reading class notes, some by solving practice problems, and some by social collaboration. Beyond blending storytelling, social learning, and supplementary tech skills content, Afrilearn leverages artificial intelligence to give every child access to personalized learning using the unique method that works best for them. This can be solved using AI recommendation systems. The recommender system provides course recommendations based on user history and similar profiles.

This repo is deployed as a web app and api through Heroku [here](https://unicef-afrilearn-app.herokuapp.com/).

## Installation
Clone this repository. Navigate to the repository and create a python virtual environment through your method of choosing. Activate the environment and install the required libraries through
```
git clone https://github.com/Afrilearn/UNICEF-AI-Personalisation.git
cd UNICEF-AI-Personalisation
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Architecture
```bash
app.py --> templates/index.html --> recommender.py --> templates/results.html
```
> - app.py opens the user interface for collecting student course levels, subjects and lessons.

> - index.html is the user interface for collecting student course levels, subjects and lessons used in calling the machine learning recommender system.

> - recommender.py loads pickle files containing the recommender system apriori rules and applies this in recommending similar lessons for students based on the student course levels, subjects and lessons.

> - results.html displays the dataframe results in html.

> - To use this app as an API, a POST reuquest can be sent directly to https://unicef-afrilearn-app.herokuapp.com/recommend with a json file containing student details for the school_level, subject and lesson.

## Dependencies
The backend is developed in python 3.x.x. Other libraries and packages, along with their versions, are included in [requirements.txt]('../../requirements.txt'). In short, you need the following libraries and their dependencies.
- pandas
- numpy
- flask_cors
- flask
- mlxtend

## Usage
<a href="https://unicef-afrilearn-app.herokuapp.com/">visit web app</a>
