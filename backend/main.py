from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
import wikipedia

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NASA_API_KEY = "DEMO_KEY" # Use your own API key

wikipedia.set_lang("pl")


# In the future - sql database or NoSQL database
planets_db = [
    {
        "name": "Merkury",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mercury_in_true_color.jpg/600px-Mercury_in_true_color.jpg",
        "desc": "Ładowanie opisu..."
    },
    {
        "name": "Wenus",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Venus-real_color.jpg/600px-Venus-real_color.jpg",
        "desc": "Ładowanie opisu..."
    },
    {
        "name": "Ziemia",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/600px-The_Earth_seen_from_Apollo_17.jpg",
        "desc": "Ładowanie opisu..."
    },
    {
        "name": "Mars",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/02/OSIRIS_Mars_true_color.jpg/600px-OSIRIS_Mars_true_color.jpg",
        "desc": "Ładowanie opisu..."
    },
    {
        "name": "Jowisz",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2b/Jupiter_and_its_shrunken_Great_Red_Spot.jpg/600px-Jupiter_and_its_shrunken_Great_Red_Spot.jpg",
        "desc": "Ładowanie opisu..."
    },
     {
        "name": "Saturn",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/800px-Saturn_during_Equinox.jpg",
        "desc": "Ładowanie opisu..."
    }
]


# I used an old FastAPI feature for educational purposes - will be replaced in the future
@app.on_event("startup")
async def load_wikipedia_data():
    print("Pobieranie dane z Wikipedii...")
    for planet in planets_db:
        try:
            # to keep it simple, we fetch only the first 2 sentences of the summary
            summary = wikipedia.summary(planet["name"], sentences=2)
            planet["desc"] = summary
            print(f"Pobrano opis dla: {planet['name']}")
        except Exception as e:
            print(f"Błąd dla {planet['name']}: {e}")
            planet["desc"] = "Nie udało się pobrać opisu z Wikipedii."

@app.get("/apod")
async def get_apod(date: str = None):
    url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": NASA_API_KEY}
    if date:
        params["date"] = date
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        return response.json()

@app.get("/planets")
async def get_planets():
    return planets_db