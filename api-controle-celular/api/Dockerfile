FROM registry.access.redhat.com/ubi8/ubi

COPY ./requirements.txt /tmp/requirements.txt

RUN mkdir -p /api && mkdir -p /venv
COPY . /api

RUN dnf install -y git && \
    dnf install -y python36 && \
    adduser \
    --no-create-home \
    --system \
    --shell /usr/sbin/nologin \
    python-server && \
    python3 -m venv /venv && \
    source /venv/bin/activate && \
    python3 -m pip install --upgrade pip && \
    pip3 install --no-cache-dir --upgrade -r /tmp/requirements.txt --no-cache-dir && \
    chown -R python-server /api && \
    chown -R python-server /venv

USER python-server

WORKDIR /api

EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"].