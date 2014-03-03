"""
sqlalchemy models for persisting data in the database.
"""
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension


Base = declarative_base()
DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


class Task(Base):
    """
    A model with a name and description used to demo how to integrate
    Cornice and sqlalchemy.
    """
    __tablename__ = 'task'
    task_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)

    @classmethod
    def from_json(cls, data):
        """Takes a dict and returns a new instance of Task."""
        return cls(**data)

    def to_json(self):
        """Returns a dict with the values of the Task."""
        to_serialize = ['task_id', 'name', 'description']
        d = {}
        for attr_name in to_serialize:
            d[attr_name] = getattr(self, attr_name)
        return d

