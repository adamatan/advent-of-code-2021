FROM python:3.10-bullseye

RUN pip install --upgrade pip

COPY requirements.txt /tmp
COPY test_requirements.txt /tmp
RUN pip install -r /tmp/test_requirements.txt -r /tmp/requirements.txt

COPY *.py /app/
COPY input /app/input

WORKDIR /app

