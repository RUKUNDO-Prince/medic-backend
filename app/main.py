from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.routes.users import router as users_router
from app.routes.auth import router as auth_router
from app.routes.inventory import router as inventory_router
from app.utils.logger import setup_logger

# Setup logger
logger = setup_logger(__name__)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware to log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Medical Inventory API"}
