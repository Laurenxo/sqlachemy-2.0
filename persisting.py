from models import User, Comment
from main import session

user_1 = User(
    user_name='Jona',
    email='jona@yopmail.com',
    comments=[
        Comment(text="Hello wWorld"),
        Comment(text="Please subscribe")
    ]
)

paul = User(
    user_name='Paul',
    email='paul@yopmail.com',
    comments=[
        Comment(text="What's up"),
        Comment(text="Please subscribe")
    ]
)

cathy = User(
    user_name='cathy',
    email='cathy@yopmail.com',
)


session.add_all([user_1, paul, cathy])
session.commit()
