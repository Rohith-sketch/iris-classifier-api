from fastapi.testclient import TestClient
from app.main import app

# 1. Turn on the Robot
client = TestClient(app)

# 2. Test the Front Door
def test_health():
    r = client.get("/")  # Changed to "/" to match your health.py router!
    assert r.status_code == 200

# 3. Test the Bouncer (Bad Data)
def test_predict_invalid():
    # Sending text instead of numbers
    r = client.post("/predict", json={"sepal_length": "oops"})
    assert r.status_code == 422 # Expecting the Bouncer to reject it!