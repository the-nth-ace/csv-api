import uvicorn
from fastapi import FastAPI
from routers.root import router
from routers.series import router as series_router


app = FastAPI()

app.include_router(router)
app.include_router(series_router, prefix="/series")

# Add routers here


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
