from fastapi import FastAPI
from routers import leave_router, pod_router, tile_router, auth_router
from auth import get_current_user

app = FastAPI()

app.include_router(leave_router)
app.include_router(pod_router)
app.include_router(tile_router)
app.include_router(auth_router)

@app.get("/api/auth/user")
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user