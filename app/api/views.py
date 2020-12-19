from typing import Dict

from fastapi import APIRouter

from api.sample_module.sample_api import sample_data_read


router = APIRouter()


@router.get("/health/", tags=["health"])
async def health() -> Dict[str, int]:
    return {"status": "Ok"}


@router.get("/sample/data-get/{id}", tags=["sample"])
async def view_sample_data(id: int):
    return sample_data_read(id)
