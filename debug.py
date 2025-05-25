import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

print("Entering ipdb session. Models available: Company, Dev, Freebie, session")
ipdb.set_trace()