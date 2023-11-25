from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserPostIn(BaseModel):
    body: str

    class Config:
        orm_mode = True

class UserPost(UserPostIn):
    id: int

class CommentIn(BaseModel):
    body: str
    post_id: int

class Comment(CommentIn):
    id: int

    class Config:
        orm_mode = True

class UserPostWithComments(BaseModel):
    post: UserPost
    comments: list[Comment]

{
"post": {"body": "Hello World", "id": 0}, 
"comments": [{"body": "Nice post!", "id": 2, "post_id": 0}]
}
