from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from src.infra.orm.repository import athlete_repository
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
