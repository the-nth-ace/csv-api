
from typing import List
from app.schemas.series import SeriesSchema
from app.repository.series_repository import add_many_series, series_helper


def get_rows(file):
    return file.decode("utf-8").splitlines()


async def schema_dictionary_helper(values: List[str]):
    """
    This function takes a list of values and converts them to
    series schema dictionary

    For example
    schema_dictionary_helper(["A", "B", "C", "D","E", "F", "G", ...])

    output:
        {
            "reference" : "A",
            "period" : "B",
            "value" : c,
            ...
        }

    """
    keys = list(SeriesSchema.__fields__.keys())
    series_data = {}

    for key, value in zip(keys, values):
        series_data[key] = value.strip()

    return SeriesSchema.parse_obj(series_data).dict()


async def add_rows_to_database(rows: List[str]):
    rows_mod = [await schema_dictionary_helper(row.split(",")) for row in rows]
    return await add_many_series(rows_mod)


async def add_series_from_csv_file(file):
    content = await file.read()
    rows = get_rows(content)
    return await add_rows_to_database(rows[1:])
