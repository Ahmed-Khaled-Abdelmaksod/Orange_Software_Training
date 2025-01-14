from flask_sqlalchemy import SQLAlchemy
from flask_injector import inject
import uuid
from app.models.blog import blog


class BlogService:
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def get_all(self):
        return blog.query.all()

    def create(self, id,title, description,likes,dislikes,author_id):
        added_blog = blog( id = id,title = title, description = description,author_id=author_id, likes = likes,dislikes = dislikes)
        self.db.session.add(added_blog)
        self.db.session.commit()

    def get_by_id(self, id):
        return blog.query.filter_by(id=id).first()

    def update(self, blog, title, description,likes,dislikes):
        blog.title = title
        blog.description = description
        blog.likes = likes
        blog.dislikes = dislikes
        self.db.session.commit()
    def inc_likes(self,id):
        needed_blog = blog.query.filter_by(id=id).first()
        needed_blog.likes = needed_blog.likes  + 1
        self.db.session.commit()
    def inc_dislikes(self,id):
        needed_blog = blog.query.filter_by(id=id).first()
        needed_blog.dislikes = needed_blog.dislikes + 1
        self.db.session.commit()

    def delete(self, blog):
        self.db.session.delete(blog)
        self.db.session.commit()

