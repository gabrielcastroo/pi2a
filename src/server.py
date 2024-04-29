from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.orm.repository import athlete_repository,match_repository
from src.infra.orm.config import database
from src.schemas import schemas
from src.infra.orm.config.database import get_db, create_db

create_db()

app = FastAPI()

@app.get('/is_running')
def is_running():
    return {"running": True}

@app.get('/')
def homepage():
    return {"homepage": "this is a homepage"}

@app.get('/athletes')
def get_athletes_controller(db: Session = Depends(get_db)):
    athletes = athlete_repository.AthleteRepository(db=db).get_athletes()
    return athletes

@app.get('/athlete/{id}')
def get_athlete_controller(id:int, db: Session = Depends(get_db)):
    athlete = athlete_repository.AthleteRepository(db=db).get_athlete(id)
    return athlete

@app.post('/athlete')
def create_athlete_controller(athlete: schemas.AthleteDTO, db: Session = Depends(get_db)):
    athlete = athlete_repository.AthleteRepository(db=db).create(athlete=athlete)
    return athlete

@app.delete("/athlete/{athlete_id}")
def delete_athlete_controller(athlete_id: int, db: Session = Depends(get_db)):
    athlete_repo = athlete_repository.AthleteRepository(db)
    athlete = athlete_repo.get_athlete(athlete_id)
    if not athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    athlete_repo.delete_athlete(athlete_id)
    return {"message": "Athlete deleted successfully"}

@app.put("/athlete/{athlete_id}")
def update_athlete_controller(athlete_id: int, athlete: schemas.AthleteDTO, db: Session = Depends(get_db)):
    athlete_repo = athlete_repository.AthleteRepository(db)
    existing_athlete = athlete_repo.get_athlete(athlete_id)
    if not existing_athlete:
        raise HTTPException(status_code=404, detail="Athlete not found")
    return athlete_repo.update_athlete(athlete_id, athlete)

@app.get('/matches')
def get_matches_controller(db: Session = Depends(get_db)):
    matches = match_repository.MatchRepository(db=db).get_matches()
    return matches

@app.get('/match/{id}')
def get_match_controller(id:int, db: Session = Depends(get_db)):
    match = match_repository.MatchRepository(db=db).get_match(id)
    return match

@app.post('/match')
def create_match_controller(match: schemas.MatchDTO, db: Session = Depends(get_db)):
    match = match_repository.MatchRepository(db=db).create(match=match)
    return match

@app.delete("/match/{match_id}")
def delete_match_controller(match_id: int, db: Session = Depends(get_db)):
    match_repo = match_repository.MatchRepository(db)
    match = match_repo.get_match(match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    match_repo.delete_match(match_id)
    return {"message": "Match deleted successfully", "match": match}

@app.put("/match/{match_id}")
def update_match_controller(match_id: int, match_dto: schemas.MatchDTO, db: Session = Depends(get_db)):
    match_repo = match_repository.MatchRepository(db)
    match = match_repo.get_match(match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match_repo.update_match(match_id, match_dto)
