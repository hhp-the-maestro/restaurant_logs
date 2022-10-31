FROM python:3.9-slim-buster

WORKDIR /app

COPY . .

RUN python unit_test.py

CMD ["python", "log_reader.py", "--filename", "log.csv"]