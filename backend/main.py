from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import httpx
import wikipedia
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager

# Importujemy nasze nowe pliki bazy danych
from database import SessionLocal, engine, Base
import models

# To polecenie tworzy plik planets.db i tabele, jeśli ich jeszcze nie ma
Base.metadata.create_all(bind=engine)

NASA_API_KEY = "DEMO_KEY" # Pamiętaj, żeby wpisać swój klucz!
wikipedia.set_lang("pl")

# --- LISTA STARTOWA ---
planets_list_init = [
    {"name": "Merkury", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mercury_in_true_color.jpg/600px-Mercury_in_true_color.jpg"},
    {"name": "Wenus", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Venus-real_color.jpg/600px-Venus-real_color.jpg"},
    {"name": "Ziemia", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/600px-The_Earth_seen_from_Apollo_17.jpg"},
    {"name": "Mars", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/600px-OSIRIS_Mars_true_color.jpg"},
    {"name": "Jowisz", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg/600px-Jupiter_and_its_shrunken_Great_Red_Spot.jpg"},
    {"name": "Saturn", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/800px-Saturn_during_Equinox.jpg"}
]

# --- LIFESPAN (Uruchamia się raz przy starcie serwera) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    db = SessionLocal()
    existing_planets = db.query(models.Planet).count()
    
    if existing_planets == 0:
        print("📭 Baza pusta! Pobieram dane z Wikipedii i zapisuję do SQL...")
        for item in planets_list_init:
            try:
                desc = wikipedia.summary(item["name"], sentences=2)
                new_planet = models.Planet(
                    name=item["name"],
                    image_url=item["image"],
                    description=desc
                )
                db.add(new_planet)
                print(f"✅ Zapisano do bazy: {item['name']}")
            except Exception as e:
                print(f"❌ Błąd Wiki dla {item['name']}: {e}")
                
        db.commit() # Zatwierdzamy zapisy!
        print("💾 Sukces! Wszystkie planety są w bazie.")
    else:
        print("📂 Dane już są w bazie SQL. Błyskawiczny start!")
    
    db.close()
    yield # Tu serwer zaczyna normalnie działać

# Inicjalizacja aplikacji
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Funkcja pomocnicza: daje dostęp do bazy w endpointach ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTY ---
@app.get("/apod")
async def get_apod(date: str = None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    if date: params["date"] = date
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()

@app.get("/planets")
def read_planets(db: Session = Depends(get_db)):
    # Pobieramy wszystko prosto z bazy danych
    planets = db.query(models.Planet).all()
    
    # Pakujemy to w taki format, jakiego oczekuje Twój React (Planets.jsx)
    response = []
    for p in planets:
        response.append({
            "name": p.name,
            "image": p.image_url,
            "desc": p.description
        })
    return response