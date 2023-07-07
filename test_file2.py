from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.mark.asyncio
async def test_check_status_other_file(client):
    assert not client.get("/my_state/").json()["state"]
