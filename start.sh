#!/usr/bin/env bash

export SECRET_KEY="moringa12"
export DATABASE_URL='postgres://ismjbvjknlmqit:c50ef7393dc91ce91fd367fd53315e87b5d98e882ca2be921da53c105b5a2d2f@ec2-54-235-66-81.compute-1.amazonaws.com:5432/dd5mfg343rhl9d'




python manage.py server
