from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session, joinedload
from database import Base, engine, get_db
from models import User, Post # Comment, Tag
from schemas import User as UserSchema, Post as PostSchema
from typing import List, Optional

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Generic Querying Mechanism 
def get_query_options(include: Optional[str] = None):
    options = []
    if include:
        for item in include.split(","):
            if item == "tags":
                options.append(joinedload(Post.tags))
            elif item == "user":
                options.append(joinedload(Post.user))
            elif item == "comments":
                options.append(joinedload(Post.comments))
            elif item == "posts":
                options.append(joinedload(User.posts))
    return options

# Endpoints
@app.get("/api/posts", response_model=List[PostSchema])
def get_posts(status: Optional[str] = None, include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    query = db.query(Post)
    if status:
        query = query.filter(Post.status == status)
    options = get_query_options(include)
    if options:
        query = query.options(*options)
    return query.all()

@app.get("/api/posts/{post_id}", response_model=PostSchema)
def get_post(post_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    options = get_query_options(include)
    query = db.query(Post).filter(Post.id == post_id)
    if options:
        query = query.options(*options)
    return query.first()

@app.get("/api/users/{user_id}", response_model=UserSchema)
def get_user(user_id: int, include: Optional[str] = Query(None), db: Session = Depends(get_db)):
    options = get_query_options(include)
    query = db.query(User).filter(User.id == user_id)
    if options:
        query = query.options(*options)
    return query.first()