FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt


CMD python3 /app/declarative_crud.py
