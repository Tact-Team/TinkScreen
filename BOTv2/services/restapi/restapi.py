import aiohttp

from my_errors import ApiError, TOKEN_ERROR, USER_EXISTS, USER_ERROR
from services.restapi.URLS import URL_USER
from services.restapi.scripts import get_headers


async def api_create_user(tg_id: int, name: str):
    headers = await get_headers()
    async with aiohttp.ClientSession(headers=headers) as session:
        body = {
            "tg_id": tg_id,
            "name": name,
        }
        async with session.post(URL_USER, json=body) as resp:
            data = await resp.json()
            if resp.status != 200 and data["ErrorID"] == 1101:
                raise ApiError(USER_EXISTS)
            if resp.status != 200:
                raise ApiError(USER_ERROR)
            return data


async def api_get_user(tg_id: int):
    headers = await get_headers()
    params = {"id_type": "student_tg"}
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(f"{URL_USER}/{str(tg_id)}",  params=params) as resp:
            data = await resp.json()
            if resp.status != 200:
                raise ApiError(USER_ERROR)
            return data


