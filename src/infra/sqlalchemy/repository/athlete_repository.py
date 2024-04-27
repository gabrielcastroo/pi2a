from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class AthleteRepository():
    def __init__(self, db: Session):
        self.db = db
    
    def create(self, athlete: schemas.AthleteDTO):
        db_athlete = models.Athlete(
            name = athlete.name,
            birth_date = athlete.birth_date,
            country = athlete.country,
            height = athlete.height,
            weight = athlete.weight,
            best_times = athlete.best_times,
            team = athlete.team,
            specializations = athlete.specializations,
            medal_history = athlete.medal_history,
            modality = athlete.modality
        )
        self.db.add(db_athlete)
        self.db.commit()
        return db_athlete

    def get_athletes(self):
        athletes = self.db.query(models.Athlete).all()
        return athletes

    def delete_athlete(self):
        pass

    def get_athlete(self):
        pass