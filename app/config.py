import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+mysqlconnector://{os.environ.get('DB_USER', 'root')}:"
        f"{os.environ.get('DB_PASSWORD', 'root')}@"
        f"{os.environ.get('DB_HOST', '127.0.0.1')}:"
        f"{os.environ.get('DB_PORT', 3306)}/"
        f"{os.environ.get('DB_NAME', 'footballdb')}"
    )
