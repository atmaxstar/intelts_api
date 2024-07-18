import os
from fastapi import FastAPI
from pcm import PunctuationCapitalizationAPI
from schemas import TextBody, TextsBody
from . import config
from functools import lru_cache

app = FastAPI()

@lru_cache()
def get_settings():
    return config.Settings()

def verify_api_key(x_api_key: str = Header(), settings: config.Settings = Depends(get_settings)):
    if x_api_key != settings.api_key:
        raise HTTPException(status_code=403, detail="Forbidden: Invalid API Key")

ml = PunctuationCapitalizationAPI()

@app.post('/punctuation-and-capitalization', dependencies=[Depends(verify_api_key)])
async def online_punctuate_and_capitalize(data: TextBody):
    result = ml.punctuate_and_capitalize(data.data)
    return {"result": result}

@app.post('/punctuation-and-capitalization/multiple', dependencies=[Depends(verify_api_key)])
async def online_punctuate_and_capitalize_multiple(data: TextsBody):
    result = ml.punctuate_and_capitalize_multiple(data.data)
    return {"result": result}
