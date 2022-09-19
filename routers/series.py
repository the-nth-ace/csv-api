from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from schemas.series import ErrorResponseModel, ResponseModel, SeriesSchema
from repository.series_repository import (
    add_series,
    retrieve_series,
    retrieve_series_by_id,
    update_series,
    delete_series,
)

# from services.series import (
#     add_series,
#     retrieve_many_series,
#     retrieve_series_by_id,
#     update_series,
#     delete_series,
# )


router = APIRouter(tags=["Series"])


@router.post("/", response_description="Series added sucessfully")
async def add_series_data(series: SeriesSchema = Body(...)):
    series = jsonable_encoder(series)
    new_series = await add_series(series)
    return ResponseModel(new_series, "Sereies added successfully")


@router.get("/")
async def get_many_series():
    return await retrieve_series()
