import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    """Test client fixture for FastAPI app"""
    return TestClient(app)

@pytest.fixture
def expected_activities():
    """Fixture containing the expected activity data"""
    return [
        {
            "activity": "Escalade à Aston, secteur Coudène, Samedi 09 Août.",
            "date": "2025-08-09"
        },
        {
            "activity": "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost, le 13 juin 2025",
            "date": "2025-06-13"
        }
    ]
