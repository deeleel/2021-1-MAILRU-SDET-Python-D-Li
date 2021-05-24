from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Requests(Base):
    __tablename__ = 'requests'

    def __repr__(self):
        return f"<Requests(" \
               f"count = '{self.count}'" \
               f")>"
    count = Column(Integer, primary_key=True)


class RequestTypes(Base):
    __tablename__ = 'requestTypes'

    def __repr__(self):
        return f"<RequestTypes(" \
               f"name = '{self.name}'," \
               f"count = '{self.count}'" \
               f")>"
    name = Column(String(500), primary_key=True)
    count = Column(Integer, nullable=False)


class PopularRequests(Base):
    __tablename__ = 'popularRequests'

    def __repr__(self):
        return f"<PopularRequests(" \
               f"url = '{self.url}'," \
               f"count = '{self.count}'" \
               f")>"
    url = Column(String(500), primary_key=True)
    count = Column(Integer, nullable=False)


class Err4Requests(Base):
    __tablename__ = 'err4Requests'

    def __repr__(self):
        return f"<Err4Requests(" \
               f"id = '{self.id}'," \
               f"url = '{self.url}'," \
               f"status = '{self.status}'," \
               f"weight = '{self.weight}'," \
               f"ip = '{self.ip}'" \
               f")>"
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(500), primary_key=True)
    status = Column(String(3))
    weight = Column(Integer, nullable=False)
    ip = Column(String(30))


class Err5Requests(Base):
    __tablename__ = 'err5Requests'

    def __repr__(self):
        return f"<Err5Requests(" \
               f"id = '{self.id}'," \
               f"ip = '{self.ip}'," \
               f"count = '{self.count}'" \
               f")>"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30))
    count = Column(Integer, nullable=False)



