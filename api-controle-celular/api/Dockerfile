FROM python:3.6

RUN adduser \
    --no-create-home \
    --system \
    --shell /usr/sbin/nologin \
    python-server && \
    mkdir -p /api && \
    chown -R python-server /api

USER python-server

WORKDIR /api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"].