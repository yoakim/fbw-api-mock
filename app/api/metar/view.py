from fastapi import APIRouter, HTTPException, Depends
from pydantic.dataclasses import dataclass
from pydantic import validator
from .fetchers import vatsim
import re

router = APIRouter()
icao = {
    'regex': '[A-Za-z]{4}',
    'status_code': 422,
    'detail': 'faulty icao codeeee'
    }
sources = {
    'test':[
        {
            'name': 'vatsim',
            'function': vatsim,
        }
    ],
    'status_code': 422,
    'detail': 'faulty source'
}

def raise_exception(p):
    raise HTTPException(status_code=p['status_code'], detail=p['detail'])

@dataclass
class MyQueryParams:
    source: str
    icao: str

    
    @validator('icao')
    def check_icao(cls, v):
        if not re.match(icao['regex'], v):
            raise_exception(icao)
        else:
            return v
    
    @validator('source')
    def check_source(cls, v):
        if not any(d['name'] == v.lower() for d in sources['test']):
            raise_exception(sources)
        else:
            return v

@router.get("/")
def metar(params: MyQueryParams = Depends(MyQueryParams)):
    for source in sources['test']:
        if source['name'] == params.source:
            return source['function'](params.icao)

