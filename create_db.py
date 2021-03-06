from sqlalchemy import create_engine
from models import Base
from sqlalchemy.engine.url import URL

DB_NAME = "rutaaccesible"

my_DB = URL(drivername='mysql', host='localhost',
            query={'read_default_file': '~/.my.cnf'}
            )

engine = create_engine(my_DB)
engine.execute("CREATE DATABASE " + DB_NAME)
engine.execute("USE " + DB_NAME)
Base.metadata.create_all(engine)
