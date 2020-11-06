FROM python:3.8.2-alpine
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add --no-cache gcc libc-dev make libffi-dev python3-dev libxml2-dev libxslt-dev postgresql-dev jpeg-dev zlib-dev musl-dev
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
COPY . /usr/src/app/