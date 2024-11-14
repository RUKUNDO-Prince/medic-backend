from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router
from app.routes.inventory import router as inventory_router

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with explicit names
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Medical Inventory API"}
