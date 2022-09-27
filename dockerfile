# syntax=docker/dockerfile:1
FROM rasa/rasa:3.2.9-full
ENV  PYTHONPATH="/app/rasaaddons:${PYTHONPATH}"