import pytest

from tests.test_main import async_client

import starlette.status

@pytest.mark.asyncio
async def test_create_and_read(async_client):
    response = await async_client.post("/users", json={"name": "myuser"})
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert response_obj["name"] == "myuser"

    response = await async_client.get("/users")
    assert response.status_code == starlette.status.HTTP_200_OK
    response_obj = response.json()
    assert len(response_obj) == 1
    assert response_obj[0]["name"] == "myuser"