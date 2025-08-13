import pytest

def test_root_endpoint_returns_activity_recording(client, expected_activities):
    """Test that GET / returns the hard-coded activity recording list"""
    response = client.get("/")
    
    # Check status code
    assert response.status_code == 200
    
    # Check response matches expected data exactly
    data = response.json()
    assert data == expected_activities

def test_root_endpoint_structure(client):
    """Test that the root endpoint returns the expected structure"""
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    
    # Check each activity has required fields
    for activity in data:
        assert "activity" in activity
        assert "date" in activity
        assert isinstance(activity["activity"], str)
        assert isinstance(activity["date"], str)

def test_fishing_endpoint(client):
    """Test the fishing endpoint"""
    response = client.get("/fishing")
    
    assert response.status_code == 200
    data = response.json()
    assert "activity fishing" in data
    assert data["activity fishing"] == "Pêche avec mon père et Clément Latapie, sur le Gave d'Azun près d'Argelès-Gazost"
