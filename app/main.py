from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.auth import get_current_user
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

# Middleware to log requests
@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Get database session
    db = next(get_db())
    logger = DatabaseLogger(db)
    
    # Get client IP
    ip_address = request.client.host
    
    # Log request
    logger.info(
        f"Incoming request",
        method=request.method,
        path=str(request.url.path),
        ip_address=ip_address
    )
    
    # Process request
    response = await call_next(request)
    
    # Log response
    logger.info(
        f"Request completed",
        method=request.method,
        path=str(request.url.path),
        status_code=response.status_code,
        ip_address=ip_address
    )
    
    return response

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])

@app.get("/")
async def root(db: Session = Depends(get_db)):
    logger = DatabaseLogger(db)
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Medical Inventory API"}
