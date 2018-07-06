#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://ohtczhixlrlvuk:cfcb0f7dfec9d1ee4b06bbecd48b2a8151bb66eaccb3ee769f5991df5e3a1d24@ec2-107-22-241-243.compute-1.amazonaws.com:5432/d8kolhlbs6rui4'


python manage.py server
