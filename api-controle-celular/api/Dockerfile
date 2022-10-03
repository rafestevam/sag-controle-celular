FROM python:3.6
WORKDIR /api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
RUN mkdir -p /api/static/documents
RUN mkdir -p /api/static/files
CMD ["flask", "run", "--host", "0.0.0.0"]