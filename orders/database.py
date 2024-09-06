from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from django.conf import settings

engine = create_engine(settings.DATABASE_URL)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)