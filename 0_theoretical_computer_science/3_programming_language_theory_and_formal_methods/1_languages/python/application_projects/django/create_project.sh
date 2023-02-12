#!/bin/zsh
'''
    quick utility to create Django project.
    accepts project name as parameter
    Example:
    $ ./create_project.sh my_app
'''

project=$1
mkdir $project
cp run_project.sh $project
cd $project

echo "creating virtual environment $project and installing Django"
pipenv install django 
echo "done"

echo "install Debug tool bar"
pipenv install django-debug-toolbar
echo "done"

echo "creating Django project called $project"
pipenv run django-admin startproject $project .
echo "done"

