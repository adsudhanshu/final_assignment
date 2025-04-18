from app.models import User
from app.schemas import UserCreate
from app.utils import generate_token

class AuthService:
    def create_admin_user(self):
        admin_user = User(username="admin", password="admin", role="admin")
        db.session.add(admin_user)
        db.session.commit()
        return admin_user

    def login(self, username: str, password: str):
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            token = generate_token(user)
            return token
        return None

    def fetch_current_user_details(self, token: str):
        user = User.query.filter_by(token=token).first()
        if user:
            return user
        return None