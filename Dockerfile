FROM python:3.9-slim-buster

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

EXPOSE 8000

COPY main.py .

CMD python3 main.py
