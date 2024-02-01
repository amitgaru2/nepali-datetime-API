FROM python:3.12-slim

WORKDIR /app

COPY ./project/new_requirements.txt /app

RUN pip install -r new_requirements.txt

COPY ./project/application /app

CMD ["uvicorn", "application:app", "--host=0.0.0.0", "--port=8000"]
