import uvicorn
from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from time import monotonic


app = FastAPI()


@app.get('/test/{id}', status_code=status.HTTP_200_OK, name='бу бу бу')
async def test(id: int):
    raise HTTPException(429)
    return {'answer': f'{id}_ok'}


if __name__ == '__main__':
    uvicorn.run(
        'pz2_server:app',
        host='127.0.0.1',
        port=10005,
        reload=True,
    )
