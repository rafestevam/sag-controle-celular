FROM registry.access.redhat.com/ubi8/python-36

USER 0

RUN mkdir -p /deployment && \
    adduser  --no-create-home --system --shell /usr/sbin/nologin python-server && \
    chown -R python-server /deployment

WORKDIR /deployment

COPY ./composer/* /deployment/composer/
COPY ./models/* /deployment/models/
COPY ./parsers/* /deployment/parsers/
COPY ./resources/* /deployment/resources/
COPY ./static/* /deployment/static/
COPY app_config.py /deployment
COPY app.py /deployment
COPY blocklist.py /deployment
COPY cellphoneauth.py /deployment
COPY db.py /deployment
COPY requirements.txt /deployment

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir

USER python-server

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]