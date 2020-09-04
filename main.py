import nepali_datetime

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(
    title="Nepali Datetime",
    description="nepali datetime",
    version="1.0.2"
)


class Date(BaseModel):
    date: Optional[str] = None
    input_fmt: Optional[str] = '%Y-%m-%d'
    output_fmt: Optional[str] = '%Y-%m-%d' 


class Datetime(BaseModel):
    datetime: Optional[str] = None
    input_fmt: Optional[str] = '%Y-%m-%d %H:%M:%S.%f%z'
    output_fmt: Optional[str] = '%Y-%m-%d %H:%M:%S.%f%z' 


@app.get("/")
def nepali_datetime_api():
    return {
        "date": "/date",
        "datetime": "/datetime"
    }


@app.post("/date")
def nepali_datetime_date(date: Date):
    if date.date is None:
        result = nepali_datetime.date.today()
    else:
        result = nepali_datetime.datetime.strptime(date.date, date.input_fmt)
    return { "result":  result.strftime(date.output_fmt) }



@app.post("/datetime")
def nepali_datetime_date(datetime: Datetime):
    if datetime.datetime is None:
        result = nepali_datetime.datetime.now()
    else:
        result = nepali_datetime.datetime.strptime(datetime.datetime, datetime.input_fmt)
    return { "result":  result.strftime(datetime.output_fmt) }
