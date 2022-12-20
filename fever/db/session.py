from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fever.config import settings

master_engine = create_engine(settings.MASTER_DATABASE_URL, pool_pre_ping=True)
MasterSession = sessionmaker(autocommit=False, autoflush=False, bind=master_engine)

slave_engine = create_engine(settings.SLAVE_DATABASE_URL, pool_pre_ping=True)
SlaveSession = sessionmaker(autocommit=False, autoflush=False, bind=slave_engine)
