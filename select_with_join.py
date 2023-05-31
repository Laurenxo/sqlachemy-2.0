from main import session
from models import User, Comment
from sqlalchemy import select


statement = select(Comment).join(User).where(
    User.user_name == 'Jona'
).where(
    Comment.text == 'Hello wWorld'
)

result = session.scalars(statement).one()

print(result)
