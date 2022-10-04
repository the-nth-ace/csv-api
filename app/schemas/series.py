from enum import Enum
from typing import Any
from pydantic import BaseModel, Field


class StatusEnum(str, Enum):
    F = "F"
    R = "R"
    C = "C"


class SeriesResponse(BaseModel):
    id: Any
    reference: str
    period: str
    value: float
    suppressed: str
    status: StatusEnum
    unit: str
    magnitude: int
    subject: str
    group: str
    series_title: str
    series_title_2: str
    series_title_3: str
    series_title_4: str


class SeriesSchema(BaseModel):
    reference: str
    period: str
    value: float = Field(default="")
    suppressed: str = Field(default="")
    status: StatusEnum
    unit: str
    magnitude: int
    subject: str
    group: str
    series_title: str
    series_title_2: str
    series_title_3: str
    series_title_4: str

    class Config:
        schema_extra = {
            "example": {
                "reference": "BDCQ.SF8RSCA",
                "period": "2022.03",
                "value": 728.894,
                "suppressed": "",
                "status": "R",
                "unit": "Dollars",
                "magnitude": 6,
                "subject": "Business Data Collection - BDC",
                "group": "Industry by financial variable (NZSIOC Level 2)",
                "series_title": "Sales (operating income)",
                "series_title_2": "Education and Training",
                "series_title_3": "Current prices",
                "series_title_4": "Trend",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
