import uuid
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import urllib3
from pydantic import BaseModel
import json
import sqlite3
#from .routers import users

class Url(BaseModel):
    url: str
    id: str
    count: int = 0

shortener = FastAPI()

#shortener.include_router(users.user_router)

# Iniciar el servidor: uvicorn main:shortener --reload

@shortener.get('/')
def read_root():
    return 'shortener'


@shortener.get('/{id}')
def get_long(id: str):
    connection = sqlite3.Connection('urls_database.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT url FROM urls WHERE id = '{id}'")

    url = cursor.fetchone()

    cursor.execute(f"UPDATE urls SET count = count + 1 WHERE id = '{id}'")

    connection.commit()
    connection.close()

    

    return RedirectResponse(url=url[0])

@shortener.post('/shrink/')
async def shrink_url(url: str, alias: str = ''):
    response = urllib3.request('get',url)
    if response.status == 200:
        id = str(uuid.uuid4()).replace('-','')[:12]
        return json.dumps(dict(url=url, id=id, count=0))
    