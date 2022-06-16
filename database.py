import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, insert
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, Session, sessionmaker


def create_core():
    try:
        engine = create_engine(
            "postgresql+psycopg2://postgres:123@localhost/newdatabase",
            echo=True, pool_size=6, max_overflow=10, encoding='latin1'
        )
        conn = engine.connect()

        metadata = MetaData()

        brands = Table('brands', metadata,
                       Column('id', Integer(), primary_key=True),
                       Column('name', Text),
                       )

        models = Table('models', metadata,
                       Column('id', Integer(), primary_key=True),
                       Column('name', Text),
                       )

        cars = Table('cars', metadata,
                     Column('id', Integer(), primary_key=True),
                     Column('name', String(100)),
                     Column('title', Text, nullable=False),
                     Column('year', Integer),
                     Column('price', Integer, nullable=False),
                     Column('link', Text, nullable=False),
                     Column('created_on', DateTime(), default=datetime.now),
                     Column('model_id', ForeignKey(models.c.id)),
                     Column('brand_id', ForeignKey(brands.c.id)),
                     )

        # metadata.create_all(engine)

        # cars.drop(engine)

        # model_list = [{"name": "camry"},{"name": "corolla"},{"name": "venza"}]
        cars_list = [{"name": "tayota new2",
                      "title": "тестовая запись",
                      "year": 2012,
                      "price": 10000000,
                      "link": "asdf",
                      "model_id": 1,
                      "brand_id": 1
                      }]

        r = conn.execute(insert(cars), cars_list)

    except (Exception, Error) as error:
        print('ошибка при подключение', error)


try:
    engine = create_engine(
        "postgresql+psycopg2://postgres:123@localhost/newdatabase",
        echo=True, pool_size=6, max_overflow=10, encoding='latin1'
    )

    Base = declarative_base()

    SessionLocal = Session(bind=engine)






except (Exception, Error) as error:
    print(error)

# finally:
#     if engine:
#         eng
#         connection.close()
#         print('соединение закрыто')
