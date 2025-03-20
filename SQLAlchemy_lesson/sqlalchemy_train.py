# Возможные варианты подключения к базам данных

# URI -> "<DBMS>+<library_name>://<user>:<password>@<host>:<port>/<database_name>"
    #    "mysql+pymysql://root:rootpassword123@localhost:3306/my_database"
    #    "sqlite:///<db_name>"

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


sqla_engine = create_engine(
    url="sqlite:///example.db",
    echo=True,
    echo_pool=True,
    # pool_size=10, # на sqlite3 не сработает!!!
    # max_overflow=15, # на sqlite3 не сработает!!!
)


session_fabric = sessionmaker(
    bind=sqla_engine
)

session = session_fabric()



from sqlalchemy import (
    create_engine,
    BigInteger,
    String,
    Integer
)
from sqlalchemy.orm import (
    sessionmaker,
    declarative_base,
    mapped_column,
    Mapped
)

Base = declarative_base()


engine = create_engine(
    url="sqlite:///example.db",
    echo=True,
    echo_pool=True,
)


# Declare style
class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )  # id INTEGER PRIMARY KEY AUTOINCREMENT
    name: Mapped[str] = mapped_column(
        String(25)
    )
    age: Mapped[int] = mapped_column(
        Integer,
    )


Base.metadata.create_all(bind=sqla_engine)



# Classic mapping style
from sqlalchemy import Table, Column, String, Text, Numeric
from sqlalchemy.orm import registry

Register = registry()

metadata = Register.metadata

news_table = Table(
    'news',
    metadata,
    Column('title', String(50), unique=True),
    Column('description', Text, nullable=True),
    Column('rating', Numeric(3, 2)),
)


class News:
    def __init__(self, title: str, description: str, rating: float) -> None:
        self.title = title
        self.description = description
        self.rating = rating


Register.map_imperatively(News, news_table)

Register.create_all(bind=sqla_engine)