from sqlalchemy import func

from models import User, Order
from main import Session

# # creates new user instance and adds it to the database
# with Session() as session:
#     new_user = User(username='Peter Green', email='GP@example.com')
#     session.add(new_user)
#     session.commit()
#
# populate_db_with = [
#     ('john_doe', 'john.doe@example.com'),
#     ('sarah_smith', 'sarah.smith@gmail.com'),
#     ('mike_jones', 'mike.jones@company.com'),
#     ('emma_wilson', 'emma.wilson@domain.net'),
#     ('david_brown', 'david.brown@email.org'),
# ]
# with Session() as session:
#     users = (User(username=u[0], email=u[1]) for u in populate_db_with)
#     session.add_all(users)
#     session.commit()
#
# retrieves info from database
# with Session() as session:
#     # user = session.query(User).all()  # retrieves all users
#
#     # # below line -> filter users by the name length - need to import 'func' and use through the model('User')
#     # users = session.query(User).filter(func.length(User.username) >= 6).order_by(User.username.desc())
#     users = session.query(User).where(func.length(User.username) >= 6).order_by(User.username.desc())  # filter == where
#
#     print(', '.join(user.username for user in users))

# # update values in database
# with Session() as session:
#     user = session.query(User).filter(User.username.istartswith('melani')).first()
#
#     if user:
#         user.email = 'Melani.Seamore@example.com'
#         session.commit()
#
#     print(user.username, user.email)

# delete values from database
# with Session() as session:
#     # user_to_delete = session.query(User).filter_by(email='GP@example.com').first()
#     user_to_delete = session.query(User).filter(User.email.icontains('GP@example.com')).first()
#
#     if user_to_delete:
#         session.delete(user_to_delete)
#         session.commit()
#
#         print(f'Successfully deleted {user_to_delete.username}!')
#     else:
#         print('User does not exist!')

# # create transaction, rollback if unsuccessfully
# session = Session()
# try:
#     session.begin()
#     users = session.query(User).all()
#     session.delete(users[0])
#     print(users[4].username)
#     print('Transaction completed successfully.')
#     session.commit()
# except Exception as e:
#     session.rollback()
#     print(f'!!! ERROR - Exception \033[4m{e}\033[0m was raised !!!')  # '\033[4m...\033[0m' -> makes text underlined
# finally:
#     session.close()
#
# with Session() as session:
#     try:
#         # session.begin()
#         users = session.query(User).all()
#         session.delete(users[0])
#         print(users[4].username)
#         print('Transaction completed successfully.')
#         session.commit()
#     except Exception as e:
#         session.rollback()
#         print(f'!!! ERROR - Exception \033[4m{e}\033[0m was raised !!!')

# # adding orders to the 'orders' table
# with Session() as session:
#     session.add_all(
#         (
#             Order(user_id=16),
#             Order(user_id=19),
#             Order(user_id=17),
#             Order(user_id=18),
#             Order(user_id=17),
#             Order(user_id=15)
#         ),
#     )
#     session.commit()

# # Queries for Relationships
# with Session() as session:
#     orders = session.query(Order).order_by(Order.user_id.desc()).all()
#
#     if not orders:
#         print('No orders found')
#     else:
#         print('\n'.join(f'Order number {o.id}, Is completed: {o.is_completed}, Username: {o.user.username} with id: {o.user.id}' for o in orders))
