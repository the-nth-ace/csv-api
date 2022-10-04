from fastapi.encoders import jsonable_encoder
from app.repository.series_repository import (
    add_series as add_series_repo,
    retrieve_series,
    retrieve_series_by_id as retrieve_series_by_id_repo,
    delete_series as delete_series_repo,
    update_series as update_series_repo,
)
from app.schemas.series import ErrorResponseModel, ResponseModel, SeriesSchema


async def add_series(series: SeriesSchema):
    new_series = await add_series_repo(jsonable_encoder(series))
    return ResponseModel(new_series, "Series added sucessfully")


async def retrieve_many_series():
    return await retrieve_series()


async def retrieve_series_by_id(id: str):
    return await retrieve_series_by_id_repo(id)


async def update_series(id: str, series_data: SeriesSchema):
    updated_series = await update_series_repo(id, series_data)
    if updated_series:
        return ResponseModel(
            "Series with ID: {} name update is successful".format(id),
            "Series name updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the Series data.",
    )


async def delete_series(id):
    deleted_series = await delete_series_repo(id)
    if deleted_series:
        return ResponseModel(
            "series with ID: {} removed".format(id), "Series deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Series with id {0} doesn't exist".format(id)
    )
