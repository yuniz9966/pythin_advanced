from typing import Type

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, DataError

from SQLAlchemy_lesson.sql_queries.models import User, Role, Comment, News
from SQLAlchemy_lesson.sql_queries.db_connection import DBConnection
from SQLAlchemy_lesson.sql_queries import engine


def create_new_role(session: Session, data: dict[str, str]) -> Role:
    try:
        role = Role(**data) # Role(name="NEW ROLE")
        session.add(role)
        session.commit() # Role(name="new role")
        session.refresh(role)

        return role
    except (IntegrityError, DataError) as err:
        session.rollback()
        raise err


def get_all_roles(session: Session) -> list[Type[Role]] | None:
    all_roles = session.query(Role).all() # SELECT * FROM Role;
    # all_roles = session.query(Role.name) # SELECT role.name FROM Role;

    if all_roles:
        return all_roles

# with DBConnection(engine) as session:
#     # role_data = {
#     #     'name': 'Client',
#     # }
#     # new_role = create_new_role(session=session, data=role_data)
#     # print(f"объект успешно создан. Новая роль: {new_role.name}")
#
#     roles = get_all_roles(session=session)
#
#     for role in roles:
#          print(f"Название роли - {role.name}")


# with DBConnection(engine) as session:
#     moderators_list = session.query(
#         User.email,
#         User.rating,
#         User.role_id
#     ).filter(
#         User.role_id == 2
#     ).all()
#
#     if moderators_list:
#         for moder in moderators_list:
#             print(f"{moder.email, moder.rating, moder.role_id}")



# role = session.query(Role).one_or_none()
# print(role.id, role.name)


# role = session.query(Role).first()
# print(role.id, role.name)



# with DBConnection(engine) as session:
#     all_authors_with_rating_gt_6 = session.query(
#         User.last_name,
#         User.role_id,
#         User.rating
#     ).filter(
#         User.role_id == 3,
#         User.rating > 6
#     ).all()
#
#     for user in all_authors_with_rating_gt_6:
#         print(user.last_name, user.rating, user.role_id)



# with DBConnection(engine) as session:
#     all_users_with_W_in_surname = session.query(
#         User.last_name,
#     ).filter(
#         User.last_name.like("W%")
#     ).all()
#
#     for user in all_users_with_W_in_surname:
#         print(user.last_name)



# with DBConnection(engine) as session:
#     from sqlalchemy import and_, or_, not_
#     users_with_rating_from_4_to_6 = session.query(
#         User.email,
#         User.rating,
#         User.first_name
#     ).filter(
#         or_(
#             User.role_id == 3,
#             User.rating.between(4, 6)
#         ),
#         not_(User.first_name.like("%n%"))
#     ).all()
#
#     for author in users_with_rating_from_4_to_6:
#         print(author.email, author.rating, author.first_name)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     count_of_authors = session.query(
#         func.count(User.id)
#     ).filter(
#         User.role_id == 3
#     ).scalar()
#
#     print(f"Count of authors - {count_of_authors}")



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     avg_rating_of_authors = session.query(
#         func.avg(User.rating)
#     ).filter(
#         User.role_id == 3
#     ).scalar()
#
#     print(f"AVG rating of authors - {avg_rating_of_authors}")



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     authors_by_rating = session.query(
#         User.rating,
#         func.count(User.id).label("count_of_authors")
#     ).filter(
#         User.role_id == 3
#     ).group_by(User.rating).all()
#
#     for us in authors_by_rating:
#         print(us.rating, us.count_of_authors)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     avg_rating = session.query(
#         func.avg(User.rating)
#     ).filter(User.role_id == 3).scalar()
#
#     authors_with_avg_rating = session.query(
#         User.email, User.role_id, User.rating
#     ).filter(User.rating >= avg_rating).all()
#
#     for us in authors_with_avg_rating:
#         print(us.email, us.role_id, us.rating)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     avg_rating = session.query(
#         func.avg(User.rating)
#     ).filter(User.role_id == 3).scalar_subquery()
#
#     authors_with_avg_rating = session.query(
#         User.email, User.role_id, User.rating
#     ).filter(User.rating >= avg_rating).all()
#
#     for us in authors_with_avg_rating:
#         print(us.email, us.role_id, us.rating)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     users_with_more_than_3_news = session.query(
#         News.author_id,
#         func.count(News.id).label("count_of_news")
#     ).group_by(News.author_id).having(func.count(News.id) > 3).all()
#
#     for us in users_with_more_than_3_news:
#         print(us.author_id, us.count_of_news)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#
#     users_with_more_than_3_news = session.query(
#         News.author_id,
#         func.count(News.id).label("count_of_news")
#     ).group_by(News.author_id).having(func.count(News.id) > 3).all()
#
#     for us in users_with_more_than_3_news:
#         print(us.author_id, us.count_of_news)



# with DBConnection(engine) as session:
#     from sqlalchemy import func
#     from sqlalchemy.orm import joinedload
#
#     news_info = session.query(
#         News.title,
#         News.moderated,
#         News.author_id,
#         User.rating.label("user_rating")
#     ).join(User).filter(
#         User.rating >= 6
#     ).all()
#
#     for n in news_info:
#         print(n.title, n.moderated, n.author_id, n.user_rating)
