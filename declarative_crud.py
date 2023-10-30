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


DB_URI = 'postgresql://postgres:123@127.0.0.1:5434/postgres'
engine = create_engine(DB_URI)


Base.metadata.create_all(engine)


session = Session(engine)
qam_signal = Signal(fftsize=1024, modulation='qam64')
qpsk_signal = Signal(fftsize=127, modulation='qpsk')
bpsk_signal = Signal(fftsize=2048, modulation='bpsk')
session.add_all([qam_signal, qpsk_signal, bpsk_signal])
session.commit()
session.close()


session2 = Session(engine)
stmt = select(Signal)

db_data = session2.scalars(stmt)

for item in db_data:
    print(f'{item=}')

session2.close()
