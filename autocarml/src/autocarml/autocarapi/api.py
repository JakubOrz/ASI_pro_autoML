import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from autocarml.src.autocarml.autocarapi.routers import predictions

app = FastAPI()
app.include_router(predictions, prefix="/predictions")


@app.get("/")
def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response


if __name__ == '__main__':
    uvicorn.run("api:app", host="127.0.0.1", port=7200, log_level="info")
