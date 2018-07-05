#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://lgjghoehrxfdcj:344b0b7ab4dc803a8244fee51f35286d053ee3432ecea5bbd809bf19a5f489cf@ec2-50-16-231-2.compute-1.amazonaws.com:5432/d5d1q5hd11chbi'


python manage.py server
