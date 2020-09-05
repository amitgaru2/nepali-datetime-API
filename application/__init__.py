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
    data: str = "2077-05-10"


class DatetimeResponse(BaseModel):
    data: str = "2051-02-14 10:44:22.21234+0545"


@app.get("/date", response_model=DateResponse)
def nepali_datetime_date(input_date: str = None,
                         input_fmt: str = Query('%Y-%m-%d', alias='input-format'),
                         output_fmt: str = Query('%Y-%m-%d', alias='output-format')):
    if input_date is None:
        data = nepali_datetime.date.today()
    else:
        data = nepali_datetime.datetime.strptime(input_date, input_fmt)
    return {"data": data.strftime(output_fmt)}


@app.get("/datetime", response_model=DatetimeResponse)
def nepali_datetime_datetime(input_datetime: str = None, input_date: str = None,
                             input_fmt: str = Query('%Y-%m-%d %H:%M:%S.%f', alias='input-format'),
                             output_fmt: str = Query('%Y-%m-%d %H:%M:%S.%f', alias='output-format')):
    if input_datetime is None:
        data = nepali_datetime.datetime.now()
    else:
        data = nepali_datetime.datetime.strptime(input_date, input_fmt)
    return {"data": data.strftime(output_fmt)}
