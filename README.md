# Advanced Medical Management System

An advanced medical management system built with FastAPI, SQLAlchemy, and PostgreSQL. This system includes features like user authentication, inventory management, report generation, and user tracking. Designed to streamline medical inventory and user data management with a robust and secure API.

## Features

- **User Authentication**: Secure user login, registration, and authentication using JWT.
- **Inventory Management**: CRUD operations for managing medical inventory items.
- **Reports**: Generate reports on inventory and user activities.
- **User Tracking**: Log and track user actions within the system.
- **Database**: PostgreSQL for reliable and scalable data storage.

## Prerequisites

- Python 3.10+
- PostgreSQL
- Git

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/medical-management-system.git
   cd medical-management-system
   ```

2. **Set up a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file in the project root to store your environment variables.

   ```env
   DATABASE_URL=postgresql://username:password@localhost/medic_db
   SECRET_KEY=your_secret_key
   ```

5. **Set up PostgreSQL database**

   Open PostgreSQL and run the following commands to create the database:

   ```sql
   CREATE DATABASE medic_db;
   CREATE USER your_user WITH PASSWORD 'your_password';
   ALTER ROLE your_user SET client_encoding TO 'utf8';
   ALTER ROLE your_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE medic_db TO your_user;
   ```

6. **Run database migrations**

   ```bash
   alembic upgrade head
   ```

## Project Structure

```plaintext
medical-management-system/
├── app/
│   ├── __init__.py
│   ├── main.py             # Application entry point
│   ├── database.py         # Database configuration
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── crud/               # Database interaction functions
│   ├── routes/             # API route definitions
│   ├── utils/              # Utility functions (auth, etc.)
│   └── config.py           # Application settings
├── alembic/                # Alembic migrations
├── .env                    # Environment variables
├── README.md               # Project README
└── requirements.txt        # Project dependencies
```

## Usage

1. **Run the application**

   ```bash
   uvicorn app.main:app --reload
   ```

2. **Access the API documentation**

   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Authentication Routes

- `POST /auth/register`: Register a new user.
- `POST /auth/token`: Authenticate a user and retrieve a JWT.

### Inventory Routes

- `POST /inventory/`: Create a new inventory item.
- `GET /inventory/`: Retrieve a list of inventory items.
- `GET /inventory/{item_id}`: Retrieve a specific inventory item.
- `PUT /inventory/{item_id}`: Update an inventory item.
- `DELETE /inventory/{item_id}`: Delete an inventory item.

### Report Routes

- `GET /reports/`: Retrieve a report summary (inventory data, user activity, etc.).

## Authentication

This project uses JSON Web Tokens (JWT) for secure user authentication. Ensure to replace `SECRET_KEY` in the `.env` file with a strong, unique value.

## Configuration

Modify the following environment variables in your `.env` file:

- `DATABASE_URL`: Database connection URL for PostgreSQL.
- `SECRET_KEY`: Secret key for JWT encoding.

## Alembic Migrations

This project uses Alembic for database migrations.

1. **Generate a new migration**

   ```bash
   alembic revision --autogenerate -m "Migration message"
   ```

2. **Apply migrations**

   ```bash
   alembic upgrade head
   ```

## Testing

1. **Run Tests**

   Ensure tests are implemented for each route and CRUD operation. To execute tests:

   ```bash
   pytest
   ```

## Deployment

For production, deploy using a production-ready server like Uvicorn or Gunicorn with ASGI. Configure the server using `systemd` or Docker as per your hosting environment.

## License

This project is licensed under the MIT License.


