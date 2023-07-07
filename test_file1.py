from fastapi.testclient import TestClient
from main import app
import pytest

@pytest.mark.asyncio
async def test_check_status(client):
  client.post("/my_state/", json={"set": True})
  assert client.get("/my_state/").json()['state']
