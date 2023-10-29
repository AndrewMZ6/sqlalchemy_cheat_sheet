from sqlalchemy import create_engine
from sqlalchemy.sql import text


# db url format -> dialect+driver://username:password@host:port/database
DB_URL = "postgresql://postgres:89234037252@localhost:5432/books"
engine = create_engine(DB_URL, echo=True)

print(engine)

'''
with engine.connect() as conn:
    command = text("INSERT INTO books (title, autor, pages, published) \
                              VALUES ('Death Note', 'Hellen Geller', 4, '4.01.1993')")
    conn.execute(command)
    conn.commit()
'''


with engine.connect() as conn:
    command = text("SELECT * FROM books")
    r = conn.execute(command)
    for i in r:
        print(i)


# OUTPUT:
# Engine(postgresql://postgres:***@localhost:5432/books)
# (1, 'my little pony', 'me', 15, datetime.date(2012, 12, 1))
# (5, 'Death Note', 'Hellen Geller', 4, datetime.date(1993, 1, 4))
# (6, 'Death Note', 'Hellen Geller', 4, datetime.date(1993, 1, 4))
# (7, 'Death Note', 'Hellen Geller', 4, datetime.date(1993, 1, 4))
# (8, 'Death Note', 'Hellen Geller', 4, datetime.date(1993, 1, 4))
