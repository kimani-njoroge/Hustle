#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://zpndeqmdejoqll:c799a1fb81eaa49b5f5a0a120802027ab65e9e1956f272476464858ea1997dda@ec2-54-243-61-173.compute-1.amazonaws.com:5432/dfi1fvvkbso40n'

python manage.py server
