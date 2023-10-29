from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine, select


# Base = declarative_base()
class Base(DeclarativeBase):
    pass


class Signal(Base):
    __tablename__ = 'signals'

    id = Column(Integer, primary_key=True)
    fftsize = Column(Integer)
    modulation = Column(String)

    def __repr__(self) -> str:
        return f'Signal(id={self.id}, fftsize={self.fftsize}, modulation={self.modulation})'


DB_URI = 'postgresql://postgres:123@localhost:5434/postgres'
engine = create_engine(DB_URI, echo=True)


Base.metadata.create_all(engine)


session = Session(engine)
qam_signal = Signal(fftsize=1024, modulation='qam64')
session.add(qam_signal)
session.commit()
session.close()


session2 = Session(engine)
stmt = select(Signal)

db_data = session2.scalars(stmt)

for item in db_data:
    print(f'{item=}')

session2.close()
