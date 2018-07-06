#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://iefzokdlddgerj:5aa3ebd8cfd9a80db70e463a68147cba678aa5c00790d72a52c7bcae3adf9783@ec2-54-163-228-190.compute-1.amazonaws.com:5432/dbsfnqpskj9a8q'

python manage.py server
