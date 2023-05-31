from main import session
from models import Comment


comment = session.query(Comment).filter_by(id=1).first()

session.delete(comment)
session.commit()
