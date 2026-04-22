from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Nazwa naszego pliku z bazą danych
SQLALCHEMY_DATABASE_URL = "sqlite:///./planets.db"

# Silnik łączący Pythona z plikiem SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fabryka sesji (pozwala na dodawanie i czytanie z bazy)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Podstawa dla naszych modeli (tabel)
Base = declarative_base()