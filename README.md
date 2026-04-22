# NASA APOD Project

**NASA APOD Project** is a modern full-stack web project that allows users to explore the universe using data directly from NASA and Wikipedia. The app combines a high-performance Python backend with an interactive React frontend, featuring a persistent database for caching planetary data.

![Demo](assets/Demo.gif)

## Key Features

- **Astronomy Picture of the Day (APOD):**
  - View the daily featured image or video from NASA.
  - Interactive sidebar calendar to browse space history.
  - Innovative UI design.

- **Smart Planet Encyclopedia:**
  - A dynamic collection of information about the Solar System.
  - **Automated Data Fetching:** Planet descriptions are automatically fetched from Wikipedia and summarized using Python.

- **User Experience:**
  - Responsive design with a collapsible sidebar navigation.
  - Smooth transitions and interactive hover effects.

## Tech Stack

### Backend
- **Python 3.14**
- **FastAPI:**
- **HTTPX:**
- **Wikipedia-API:**

### Frontend
- **React (Vite):**
- **React Router:**
- **CSS3:**

---

## How to run locally?

### 1. Clone the repository
```bash
git clone https://github.com/v0yenka/NASA-Apod.git
cd nasa-apod-explorer
```

### 2. Backend setup
Navigate to the backend folder and install dependencies:
```bash
cd backend
pip install fastapi uvicorn httpx wikipedia
```
Start the server:
```bash
python -m uvicorn main:app --reload
```

### 3. Frontend setup
In a new terminal, navigate to frontend folder:
```bash
cd frontend
npm install
```
Start the server:
```bash
npm run dev
```

## Incoming Updates
- **SQL Database Integration:** Implementing **SQLite & SQLAlchemy** to cache planet data locally.
- **User Accounts:** Allowing users to create accounts and save their favorite NASA photos to a personal collection.

## API Reference

This project uses the **NASA Open API**.
You can get your own API Key at [api.nasa.gov](https://api.nasa.gov/).

To use your own key, update the `NASA_API_KEY` variable in `backend/main.py`.

---

## Author
**v0yenka**
