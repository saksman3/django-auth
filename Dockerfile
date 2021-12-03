FROM python:3.9

RUN mkdir -p /home/ssibuyi/auth_app/
RUN mkdir -p /home/ssibuyi/auth_app/logs

WORKDIR /home/ssibuyi/auth_app/

COPY . /home/ssibuyi/auth_app/

RUN pip install -r /home/ssibuyi/auth_app/requirements.txt

VOLUME /home/ssibuyi/auth_app/

RUN chmod u+x /home/ssibuyi/auth_app/bin/gunicorn_start.sh

ENTRYPOINT [ "/home/ssibuyi/auth_app/bin/gunicorn_start" ]


