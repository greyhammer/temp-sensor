#!/bin/sh
export FLASK_APP=/home/keith/temp-sensor/temp.py
pipenv run flask --debug run -h 0.0.0.0
