#!/bin/sh

flask db upgrade

gunicorn -w 2 -b 0.0.0.0:5000 run:app