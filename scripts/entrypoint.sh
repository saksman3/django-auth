#!/bin/sh

#ensure if one command fails then system exists
set -e 

uwsgi --socket :8000 --master --enable-threads --module react-auth.wsgi

