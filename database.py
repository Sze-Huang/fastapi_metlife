from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql://roy:roy@localhost/metlife"
DATABASE_URL = "mysql+mysqlconnector://metlifeadmin:Simple123@metlife.mysql.database.azure.com:3306/metlife"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
