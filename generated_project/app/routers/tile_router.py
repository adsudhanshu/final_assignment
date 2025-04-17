from fastapi import APIRouter, Depends
from services import TileService
from schemas import TileResponse

router = APIRouter()

@router.get("/api/dashboard/tiles")
async def get_tiles(db: Session = Depends()):
    tile_service = TileService(db)
    return tile_service.get_tiles()