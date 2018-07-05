#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://sknpcuciqxjcph:7342bf0cc6ad54592f4f8c5cc62d3903a1a7151de171f914153fef7f9b04f667@ec2-54-235-66-81.compute-1.amazonaws.com:5432/d2b6cvls0amoth'

python manage.py server
