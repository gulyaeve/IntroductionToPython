from sqlalchemy import create_engine, MetaData, Table, Column, INTEGER, TEXT, insert
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///my_db2.db", echo=True)

Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()

table = Table(
    "Users",
    metadata,
    Column("id", INTEGER, primary_key=True),
    Column("name", TEXT, nullable=False),
    Column("age", INTEGER)
)


if __name__ == '__main__':
    metadata.create_all(engine)

    # session.execute(table.insert().values(name="Vasya", age=18))
    # session.commit()
    x = session.execute(table.select())
    print(x.fetchall())
    # with engine.connect() as conn:
    #     x = conn.execute(table.select())
    #     print(x)
