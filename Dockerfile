FROM python:3.12-slim

WORKDIR /app

COPY ./project/new_requirements.txt /app

RUN pip install -r new_requirements.txt

ADD ./project/application /app/application

CMD ["uvicorn", "application:app", "--host=0.0.0.0", "--port=8000"]
