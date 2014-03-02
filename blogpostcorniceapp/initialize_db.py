
from sqlalchemy import engine_from_config
from blogpostcorniceapp.models import DBSession
from pyramid.paster import get_appsettings

from blogpostcorniceapp.models import Base

settings = get_appsettings('/home/fran/random/blogpostcorniceapp/blogpostcorniceapp.ini')
engine = engine_from_config(settings, 'sqlalchemy.')
DBSession.configure(bind=engine)

Base.metadata.create_all(engine)
