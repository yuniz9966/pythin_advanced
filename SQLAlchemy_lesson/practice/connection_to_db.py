from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship

URL = "sqlite:///relations.db"

engine = create_engine(URL, echo=True, echo_pool=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id: Mapped[int]=mapped_column(Integer, primary_key=True)
    name: Mapped[str]=mapped_column(String(50))
    age: Mapped[int]=mapped_column(Integer)
    news: Mapped['News'] = relationship("News", back_populates="user")


class News(Base):
    __tablename__ = "news"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str]=mapped_column(String(120))
    user_id: Mapped[int]=mapped_column(Integer, ForeignKey("users.id"))
    user: Mapped['User'] = relationship("User", back_populates="news")



Base.metadata.create_all(bind=engine)



# FOR HOMEWORK
# "sqlite:///:memory:"














