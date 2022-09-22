from fastapi import APIRouter, File, UploadFile
from services.csv_processor import add_series_from_csv_file

router = APIRouter(tags=["Root"])


@router.post("/")
async def add_many_series_from_csv(file: UploadFile):
    return await add_series_from_csv_file(file)
