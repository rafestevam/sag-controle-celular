FROM python:3.6
USER 0
WORKDIR /api
COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]