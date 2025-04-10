from __future__ import annotations
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    name: str

class User(UserBase):
    id: int
    posts: Optional[List["Post"]] = None
    comments: Optional[List["Comment"]] = None
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class Comment(CommentBase):
    id: int
    user_id: int
    post_id: int
    user: Optional[UserBase] = None
    class Config:
        orm_mode = True

class TagBase(BaseModel):
    name: str

class Tag(TagBase):
    id: int
    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    status: str

class Post(PostBase):
    id: int
    user_id: int
    user: Optional[UserBase] = None
    comments: Optional[List[Comment]] = None
    tags: Optional[List[Tag]] = None
    class Config:
        orm_mode = True

