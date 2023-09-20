from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship

association_table = Table('place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary=association_table, back_populates='amenities')

class Place(BaseModel, Base):
    __tablename__ = 'places'
    
    amenities = relationship('Amenity', secondary=association_table, back_populates='place_amenities')
