#!/bin/bash
# Name of the application
NAME="auth_app"
# Django project directory
DJANGODIR=/home/ssibuyi/auth_app/auth
# we will communicte using this unix socket
SOCKFILE=/home/ssibuyi/auth_app/auth/run/gunicorn.sock
# the user to run as
USER=ssibuyi
# the group to run as
GROUP=ubuntu
# how many worker processes should Gunicorn spawn
NUM_WORKERS=3
# which settings file should Django use
DJANGO_SETTINGS_MODULE='react-auth.settings.dev'
# WSGI module name
DJANGO_WSGI_MODULE=react-auth.wsgi
echo "Starting $NAME as `whoami`"
# Activate the virtual environment
cd $DJANGODIR
source ../bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR
# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--bind=unix:$SOCKFILE \
--log-level=debug \
--log-file=-