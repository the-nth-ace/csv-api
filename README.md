# CSV API

## 🖥️ Tech Stack
- Python 
- FastAPI
- MongoDB
- Motor
## 📃 About API

This API is used to perform simple CRUD operations on a SeriesObject, and exposes endpoints typical for such operations. In additon, it exposes an
endpoint that allows for the upload of *.csv files. This is used to bulk_add data into MongoDB.

```python
class SeriesSchema(BaseModel):
    reference: str
    period: str
    value: float | str | None = Field(default=0)
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
```

## ⚙️ To Run
- Clone the repo
- Install pipenv

    ```
    pip install pipenv
    ```
- Install dependencies

    ```
    pipenv install
    ```
* Set Environment Variable
    ```
    MONGO_URL
    ```

* Run the app
    ```
    python main.py
    ```

```smalltalk
Swagger docs: https://ace-csv-api.herokuapp.com/docs
```
