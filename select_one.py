from main import session
from models import User


jona = session.query(User).filter_by(user_name='Jona').first()

print(jona)
