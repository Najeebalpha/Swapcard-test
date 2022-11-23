# Swapcard-test


<Project Setup>

Install scoop from www.scoop.sh
Install allure commandline by running the following command:

<scoop install allure>

.git clone
.cd to project directory
.Install virtualenv:

<py -m pip install --user virtualenv>
py -m venv env

.Activate your virtual environment:
<\env\Scripts\activate>

Running Test

<pipenv run pytest --alluredir=allure-results --browser <browser>

View Help And Custom CLI Options
pytest --help


