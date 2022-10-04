from typing import Any
from fastapi import APIRouter, Body
from app.schemas.series import SeriesResponse, SeriesSchema
from fastapi_pagination import Page, add_pagination, paginate

from app.services.series import (
    add_series,
    retrieve_many_series,
    retrieve_series_by_id,
    update_series,
    delete_series,
)


router = APIRouter(tags=["Series"])


@router.post("/", response_description="Series added sucessfully")
async def add_series_data(series: SeriesSchema = Body(...)):
    return await add_series(series)


@router.get("/", response_model=Page[Any])
async def get_many_series():
    series = await retrieve_many_series()
    return paginate(series)


@router.get("/{id}", response_model=SeriesResponse)
async def get_series_by_id(id):
    return await retrieve_series_by_id(id)


@router.delete("/{id}", response_description="Series data deleted from the database")
async def delete_series_data(id: str):
    return await delete_series(id)


@router.put("/{id}")
async def update_series_data(id: str, req: SeriesSchema = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    return await update_series(id, req)


add_pagination(router)
