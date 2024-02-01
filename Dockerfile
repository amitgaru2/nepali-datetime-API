FROM python:3.12-slim

WORKDIR /app

COPY ./project/application /app

RUN pip install new_requirements.txt

CMD ["uvicorn", "application:app", "--host=0.0.0.0", "--port=8000"]
