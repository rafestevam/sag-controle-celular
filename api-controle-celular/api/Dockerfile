FROM registry.access.redhat.com/ubi8/ubi

COPY ./requirements.txt /tmp/requirements.txt

RUN dnf install -y git && \
    dnf install -y python36 && \
    python -m pip install --upgrade pip && \
    adduser \
    --no-create-home \
    --system \
    --shell /usr/sbin/nologin \
    python-server && \
    pip3 install --no-cache-dir --upgrade -r /tmp/requirements.txt && \
    mkdir -p /api && \
    chown -R python-server /api

USER python-server

WORKDIR /api

COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"].