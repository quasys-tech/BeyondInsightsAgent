# base image  
# FROM python:3.13.0a5-alpine3.19
FROM python:3.10.13-alpine

# setup environment variable  
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN python -m pip install --upgrade pip

WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app
RUN pip install -r requirements.txt

COPY . /usr/src/app

CMD ["python", "get_secrets.py"]