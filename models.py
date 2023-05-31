from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, nullable=False)
    user_name = Column(String, nullable=False)
    email = Column(String)
    comments = relationship('Comment', back_populates='user')

    def __repr__(self):
        return f"User username={self.user_name}"


class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id')) #Table name .id
    text = Column(String, nullable=False)
    user = relationship('User', back_populates='comments')

    def __repr__(self):
        return f"Comment text={self.text} by {self.user.user_name}"
