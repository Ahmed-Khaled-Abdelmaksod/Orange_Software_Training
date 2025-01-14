#BLOG CLASS for database mapping

from app import db 

class blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.email'), nullable=False)  # Foreign key linking to User

    # Define the relationship from the blog side to link to the User
    author = db.relationship('User', back_populates='blogs')