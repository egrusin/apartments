from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
# Создание сессии
engine = create_engine('postgresql://postgres:egrus@localhost:5432/apartment')
Session = sessionmaker(bind=engine)
session = Session()


class MultistoreyBuilding(Base):
    __tablename__ = 'multistorey_buildings'
    id = Column(Integer, primary_key=True)
    fias_code = Column(String)
    wall_material = Column(String)
    year_built = Column(Integer)
    area = Column(Float)
    apartments_count = Column(Integer)

    @classmethod
    def create(cls, fias_code, wall_material, year_built, area, apartments_count):
        new_building = cls(fias_code=fias_code,
                           wall_material=wall_material,
                           year_built=year_built,
                           area=area,
                           apartments_count=apartments_count)
        session.add(new_building)
        session.commit()
        return new_building

    @classmethod
    def get(cls, id):
        return session.query(cls).filter_by(id=id).first()

