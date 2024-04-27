from pydantic import BaseModel

class AthleteDTO(BaseModel):
    id: int
    name: str
    birth_date: DateTime
    country: str
    height: float
    weight: float
    best_times: list
    team: str
    specializations: list
    medal_history: list
    modality: list

class JudgeDTO(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    password: str
    country: str
    certification_level: str
    arbitration_category: list

class MatchDTO(BaseModel):
    id: int
    datetime: DateTime
    match_type: str
    distance: float
    match_status: str
    judge: list
    location: str
    athletes_involved: list
    result: str