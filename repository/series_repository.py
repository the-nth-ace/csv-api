from re import L
from bson.objectid import ObjectId
from common.database import series_collection


def series_helper(series) -> dict:
    return {
        "id": str(series["_id"]),
        "reference": str(series["reference"]),
        "period": str(series["period"]),
        "value": float(series["value"]),
        "status": str(series["status"]),
        "unit": str(series["unit"]),
        "magnitude": int(series["magnitude"]),
        "subject": str(series["subject"]),
        "group": str(series["group"]),
        "series_title": str(series["series_title"]),
        "series_title_2": str(series["series_title_2"]),
        "series_title_3": str(series["series_title_3"]),
        "series_title_4": str(series["series_title_4"]),
    }


# Retrieve all sereies in the database
async def retrieve_series():
    series = []
    async for serie in series_collection.find():
        series.append(series_helper(serie))
    return series


async def add_series(series_data: dict) -> dict:
    series = await series_collection.insert_one(series_data)
    new_series = await series_collection.find_one({"_id": series.inserted_id})
    return series_helper(new_series)


async def retrieve_series_by_id(id: str) -> dict:
    series = await series_collection.find_one({"_id": ObjectId(id)})
    if series:
        return series


async def update_series(id: str, data: dict):
    if len(data) < 1:
        return False
    series = await series_collection.find_one({"_id": ObjectId(id)})
    if series:
        updated_series = await series_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )

        if updated_series:
            return True
        return False


async def delete_series(id: str):
    series = await series_collection.find_one({"_id": ObjectId(id)})
    if series:
        await series_collection.delete_one({"_id": ObjectId(id)})
        return True
