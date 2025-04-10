from database import SessionLocal
from models import User, Post, Comment, Tag

db = SessionLocal()

user1 = User(name="VicktoR")
user2 = User(name="Kaya")

post1 = Post(title="First Post", status="draft", user=user1)
post2 = Post(title="Second Post", status="published", user=user2)

comment1 = Comment(content="Great post!", user=user2, post=post1)
comment2 = Comment(content="Thanks!", user=user1, post=post1)

tag1 = Tag(name="python")
tag2 = Tag(name="fastapi")

post1.tags.append(tag1)
post1.tags.append(tag2)

db.add_all([user1, user2, post1, post2, comment1, comment2, tag1, tag2])
db.commit()
db.close()


