from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api import views

from core.settings import config

app = FastAPI(docs_url=config.DOCS_URL, redoc_URL=config.REDOC_URL)

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.ALLOWED_HOSTS or ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(views.router, prefix=config.API_PREFIX)
