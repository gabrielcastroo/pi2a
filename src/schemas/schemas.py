from pydantic import BaseModel
from typing import Optional, List

class AthleteDTO(BaseModel):
    id: int
    name: str
    birth_date: DateTime
    country: str
    height: float
    weight: float
    best_times: Optional[list] = None
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
    associated_matches: Optional[List[MatchDTO]]

class MatchDTO(BaseModel):
    id: int
    datetime: DateTime
    match_type: str
    distance: float
    match_status: str
    judges: Optional[List[JudgeDTO]]
    location: str
    athletes_involved: List[AthleteDTO]
    result: str