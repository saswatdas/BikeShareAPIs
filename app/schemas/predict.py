from typing import Any, List, Optional

from pydantic import BaseModel

class Input_List(BaseModel):
    dteday:Optional[str]
    season: Optional[str]
    hr: Optional[str]
    holiday: Optional[str]
    weekday: Optional[str]
    workingday: Optional[str]
    weathersit: Optional[str]
    temp: Optional[float]
    atemp: Optional[float]
    hum: Optional[float]
    windspeed: Optional[float]

class Predict(BaseModel):
    inputs: List[Input_List]
    
    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "dteday" : "2012-05-11",
                        "season" : "winter",
                        "hr": "6am",
                        "holiday": "No",
                        "weekday": "Mon",
                        "workingday": "Yes",
                        "weathersit": "Mist",
                        "temp": 12.1,
                        "atemp": 3.0014,
                        "hum": 49,
                        "windspeed": 19.0012
                    }
                ]
            }
        }

class PredictionResults(BaseModel):
    version: str
    predictions: Optional[int]

