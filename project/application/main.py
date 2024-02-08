import datetime
import nepali_datetime

from pydantic import BaseModel
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="Nepali Datetime",
    description="The package similar to Python's core datetime package that operates on Bikram Sambat (B.S) "
                "date & Nepal Time +05:45.",
    version=nepali_datetime.__version__,
    redoc_url='/',
)
app.add_middleware(CORSMiddleware, allow_origins=["*"])


class DateResponse(BaseModel):
    data: str = str(nepali_datetime.date.today()) 


class DatetimeResponse(BaseModel):
    data: str = str(nepali_datetime.datetime.now()) 


@app.get("/date", response_model=DateResponse)
def nepali_datetime_date(fmt: str = Query('%Y-%m-%d', alias='format')):
    data = nepali_datetime.date.today()
    return {"data": data.strftime(fmt)}


@app.get("/date/convert/bs-ad", response_model=DateResponse)
def nepali_datetime_date_convert_bs_ad(bs_date: str = Query('2080-10-29'), fmt: str = Query("%Y-%m-%d", alias="format")):
    try:
        bs_date = nepali_datetime.datetime.strptime(bs_date, "%Y-%m-%d").date()
        ad_date = nepali_datetime.date.to_datetime_date(bs_date).strftime(fmt)
    except Exception:
        raise HTTPException(status_code=400, detail="Something wrong with your input!")
    return {"data": ad_date}


@app.get("/date/convert/ad-bs", response_model=DateResponse)
def nepali_datetime_date_convert_ad_bs(ad_date: str = Query('2024-02-12'), fmt: str = Query("%Y-%m-%d", alias="format")):
    try:
        ad_date = datetime.datetime.strptime(ad_date, "%Y-%m-%d").date()
        bs_date = nepali_datetime.date.from_datetime_date(ad_date).strftime(fmt)
    except Exception:
        raise HTTPException(status_code=400, detail="Something wrong with your input!")
    return {"data": bs_date}


@app.get("/datetime", response_model=DatetimeResponse)
def nepali_datetime_datetime(fmt: str = Query('%Y-%m-%d %H:%M:%S.%f', alias='format')):
    data = nepali_datetime.datetime.now()
    return {"data": data.strftime(fmt)}
