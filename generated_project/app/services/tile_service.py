from database import get_db
from models import Tile
from schemas import TileResponse

class TileService:
    def __init__(self, db):
        self.db = db

    def get_tiles(self):
        tiles = self.db.query(Tile).all()
        return [TileResponse.from_orm(tile) for tile in tiles]