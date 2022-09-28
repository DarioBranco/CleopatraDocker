#!/bin/bash
source ../venv/bin/activate
export PYTHONPATH=../rasaaddons:$PYTHONPATH
rasa run actions -p 5055 &
rasa run -m models --enable-api --cors "*" --debug -p 5006
