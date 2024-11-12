from fastapi import FastAPI
from app.database import engine, Base
from app.routes import auth, users, inventory  # Import your route modules here

# Initialize the FastAPI app
app = FastAPI()

# Create all tables (for development/testing - not recommended for production)
Base.metadata.create_all(bind=engine)

# Include your routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(inventory.router, prefix="/inventory", tags=["Inventory"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Medical Management System API"}
