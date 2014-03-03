"""
Main entry point
"""
from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from blogpostcorniceapp.models import DBSession


def main(global_config, **settings):
    """
    Sets up connections to the database.
    Uses Cornice to add routes.
    Returns a wsgi app.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("blogpostcorniceapp.views")
    return config.make_wsgi_app()
