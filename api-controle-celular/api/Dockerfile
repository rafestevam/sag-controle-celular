FROM registry.access.redhat.com/ubi8/python-36

WORKDIR /deployment

COPY . /deployment

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt --no-cache-dir

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]