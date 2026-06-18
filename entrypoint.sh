#!/bin/sh
set -e

flask db upgrade

python -m app.scripts.addall

gunicorn -w 2 -b 0.0.0.0:5000 run:app