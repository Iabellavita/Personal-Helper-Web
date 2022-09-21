FROM --platform=linux/amd64 python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /PH

COPY requirements.txt /PH
RUN pip install -r requirements.txt

COPY . /PH
EXPOSE 8000