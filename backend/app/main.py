from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="OutdoorCompass API",
    description="Backend API for OutdoorCompass application",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Hard-coded activity recording
activity_recording = [
    {
        "activity": "Escalade à Aston, secteur Coudène, Samedi 09 Août.",
        "date": "2025-08-09"
    },
    {
        "activity": "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost, le 13 juin 2025",
        "date": "2025-06-13"
    }
]
@app.get("/")
async def root():
    return activity_recording

@app.get("/fishing")
async def fishing_history():
    return {"activity fishing": "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
