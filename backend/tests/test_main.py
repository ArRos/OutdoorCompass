import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint_returns_activity_recording():
    """Test that GET / returns the hard-coded activity recording list"""
    response = client.get("/")
    
    # Check status code
    assert response.status_code == 200
    
    # Check response structure
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    
    # Check first activity
    first_activity = data[0]
    assert "activity" in first_activity
    assert "date" in first_activity
    assert first_activity["activity"] == "Escalade à Aston, secteur Coudène, Samedi 09 Août."
    assert first_activity["date"] == "2025-08-09"
    
    # Check second activity
    second_activity = data[1]
    assert "activity" in second_activity
    assert "date" in second_activity
    assert second_activity["activity"] == "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost, le 13 juin 2025"
    assert second_activity["date"] == "2025-06-13"

def test_root_endpoint_response_format():
    """Test that the root endpoint returns the expected JSON format"""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    data = response.json()
    
    # Verify each activity has the required fields
    for activity in data:
        assert isinstance(activity, dict)
        assert "activity" in activity
        assert "date" in activity
        assert isinstance(activity["activity"], str)
        assert isinstance(activity["date"], str)

def test_fishing_endpoint():
    """Test the fishing endpoint"""
    response = client.get("/fishing")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    data = response.json()
    assert "activity fishing" in data
    assert data["activity fishing"] == "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost"

def test_root_endpoint_activity_count():
    """Test that the root endpoint returns exactly 2 activities"""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2

def test_root_endpoint_activity_dates():
    """Test that the dates in activities are valid date strings"""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    
    for activity in data:
        date_str = activity["date"]
        # Check if date string follows YYYY-MM-DD format
        assert len(date_str) == 10
        assert date_str[4] == "-"  # First dash
        assert date_str[7] == "-"  # Second dash
        # Check if parts are numeric
        year, month, day = date_str.split("-")
        assert year.isdigit()
        assert month.isdigit()
        assert day.isdigit()

def test_root_endpoint_activity_content():
    """Test that activity descriptions are non-empty strings"""
    response = client.get("/")
    
    assert response.status_code == 200
    data = response.json()
    
    for activity in data:
        activity_desc = activity["activity"]
        assert isinstance(activity_desc, str)
        assert len(activity_desc) > 0
        assert activity_desc.strip() == activity_desc  # No leading/trailing whitespace
