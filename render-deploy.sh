#!/usr/bin/env bash
set -e

poetry run flask --app src.app2 db upgrade
poetry run gunicorn src.wsgi:app2