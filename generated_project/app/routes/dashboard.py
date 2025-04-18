from fastapi import APIRouter, Depends
from app.services import dashboard_service
from app.schemas import TileCreate

router = APIRouter()

@router.get("/tiles")
async def fetch_dashboard_data():
    tiles = dashboard_service.fetch_dashboard_data()
    return tiles