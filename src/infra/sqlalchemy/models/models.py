from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional, List
from datetime import datetime

Base = declarative_base()

class Athlete(Base):
    __tablename__ = 'athletes'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    birth_date = Column(DateTime)
    country = Column(String)
    height = Column(Float)
    weight = Column(Float)
    best_times = Column(String, nullable=True)
    team = Column(String)
    specializations = Column(String)
    medal_history = Column(String)
    modality = Column(String)

class Judge(Base):
    __tablename__ = 'judges'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String)
    password = Column(String)
    country = Column(String)
    certification_level = Column(String)
    arbitration_category = Column(String)
    associated_matches = relationship("Match", back_populates="judges")

class Match(Base):
    __tablename__ = 'matches'
    id = Column(Integer, primary_key=True, index=True)
    datetime = Column(DateTime, default=datetime.now)
    match_type = Column(String)
    distance = Column(Float)
    match_status = Column(String)
    location = Column(String)
    result = Column(String)
    judges = relationship("Judge", secondary="match_judge_association")
    athletes_involved = relationship("Athlete", secondary="match_athlete_association")

match_judge_association = Table('match_judge_association', Base.metadata,
    Column('match_id', Integer, ForeignKey('matches.id')),
    Column('judge_id', Integer, ForeignKey('judges.id'))
)

match_athlete_association = Table('match_athlete_association', Base.metadata,
    Column('match_id', Integer, ForeignKey('matches.id')),
    Column('athlete_id', Integer, ForeignKey('athletes.id'))
)
