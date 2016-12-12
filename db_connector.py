from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL


DB_NAME = "rutaaccesible"

my_DB = URL(drivername='mysql', host='localhost',
            database=DB_NAME,
            query={'read_default_file': '~/.my.cnf'}
            )

engine = create_engine(my_DB)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()