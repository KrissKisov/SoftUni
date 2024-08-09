from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'postgresql+psycopg2://myuser:mypassword@localhost:5432/sqlalchemy_lab_db'
engine = create_engine(DATABASE_URL)
# # creates DB pooling -> 10 db connections constantly open(and additional 20 temporary connections if needed) for improved DB interaction
# engine = create_engine(DATABASE_URL, pool_size=10, max_overflow=20)

Session = sessionmaker(bind=engine)
