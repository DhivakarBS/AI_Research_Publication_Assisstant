from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_endpoint() -> None:
    """The health endpoint should return the expected payload."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "ResearchAI IEEE Compliance Engine",
        "version": "1.0.0",
    }
