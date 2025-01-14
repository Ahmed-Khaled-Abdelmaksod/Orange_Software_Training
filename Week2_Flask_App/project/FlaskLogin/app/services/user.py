from sqlite3 import IntegrityError
from flask_sqlalchemy import SQLAlchemy
from flask_injector import inject
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
import uuid
from app.models.user import User


class UserService:
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_by_email(self, email):
        return User.query.get(email)

    

    def login(self, email, password):
        user = self.get_by_email(email)

        if not user or not check_password_hash(user.password, password):
            return False
        login_user(user)

        return True
    
    def is_admin(self,email):
        user = self.get_by_email(email)

        if not user or  user.role != 'Admin':
            return False
        return True
    def signup(self, name, email, password):
        user = User(
            public_id=str(uuid.uuid4()),
            name=name,
            email=email,
            password=generate_password_hash(password),
            role='Reader'
        )
        self.db.session.add(user)
        self.db.session.commit()

    def make_author(self,email):
        user = self.get_by_email(email)
        user.role = 'Author'
        self.db.session.commit()

    def logout(self):
        logout_user()


    def insert_user(self,id,public_id,email,name,password,role):
    # Check if the username already exists
        existing_user = self.db.session.query(User).filter_by(email=email).first()

        if existing_user:
            # Handle the case where the username already exists
            print(f"Email {email} already exists!")
            return "Email already exists"  # Optionally return or raise an error
        
        # If the username doesn't exist, insert the new user
        try:
            user = User(name=name,public_id=public_id, email=email, password=password, role=role)
            self.db.session.add(user)
            self.db.session.commit()
            return "User added successfully"
        except IntegrityError as e:
            self.db.session.rollback()
            print(f"Failed to insert user: {e}")
            return "Failed to insert user"

