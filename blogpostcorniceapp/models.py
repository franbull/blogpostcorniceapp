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
    __tablename__ = 'task'
    task_id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text)

    @classmethod
    def from_json(cls, data):
        return cls(**data)
