from app.models import Tile
from app.schemas import TileCreate

class DashboardService:
    def fetch_dashboard_data(self):
        tiles = Tile.query.all()
        return tiles