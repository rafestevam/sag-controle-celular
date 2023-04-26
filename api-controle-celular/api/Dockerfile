FROM python:3.6

USER 0

COPY ./requirements.txt /tmp/requirements.txt

RUN adduser \
    --no-create-home \
    --system \
    --shell /usr/sbin/nologin \
    python-server && \
    pip install --no-cache-dir --upgrade -r /tmp/requirements.txt && \
    mkdir -p /api && \
    chown -R python-server /api

USER python-server

WORKDIR /api

COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"].