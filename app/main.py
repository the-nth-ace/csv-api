import uvicorn
from fastapi import FastAPI
from app.routers.root import router
from app.routers.series import router as series_router


app = FastAPI()

app.include_router(router)
app.include_router(series_router, prefix="/series")

# Add routers here
