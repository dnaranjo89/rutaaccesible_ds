from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, Float
from db_connector import session


Base = declarative_base()

class ParkingSlot(Base):
    __tablename__ = 'parking_slot'

    session = session

    id = Column(Integer, primary_key=True)
    pos_lat = Column(Float)
    pos_lon = Column(Float)
    extra_info = Column(Text)

    def save(self, commit=True):
        session.add(self)
        if commit:
            session.commit()