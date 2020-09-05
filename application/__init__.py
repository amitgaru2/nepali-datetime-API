import nepali_datetime

from typing import Optional

from pydantic import BaseModel
from fastapi import FastAPI, Query

app = FastAPI(
    title="Nepali Datetime",
    description="The package similar to Python's core datetime package that operates on Bikram Sambat (B.S) "
                "date & Nepal Time +05:45.",
    version="1.0.2",
    redoc_url='/',
)


class DateResponse(BaseModel):
    data: str = str(nepali_datetime.date.today()) 


class DatetimeResponse(BaseModel):
    data: str = str(nepali_datetime.datetime.now()) 


@app.get("/date", response_model=DateResponse)
def nepali_datetime_date(fmt: str = Query('%Y-%m-%d', alias='format')):
    data = nepali_datetime.date.today()
    return {"data": data.strftime(fmt)}


@app.get("/datetime", response_model=DatetimeResponse)
def nepali_datetime_datetime(fmt: str = Query('%Y-%m-%d %H:%M:%S.%f', alias='format')):
    data = nepali_datetime.datetime.now()
    return {"data": data.strftime(fmt)}
