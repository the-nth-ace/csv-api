from fastapi import APIRouter, File, UploadFile
from services.csv_processor import add_series_from_csv_file

router = APIRouter()


@router.post("/")
async def read_root(file: UploadFile):
    return await add_series_from_csv_file(file)
