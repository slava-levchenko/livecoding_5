from pydantic import BaseModel, Field

class Post(BaseModel):
    user_id: int = Field(..., alias="userId")
    id: int
    title: str
    body: str


class Comment(BaseModel):
    post_id: int = Field(..., alias="postId")
    id: int
    name: str
    email: str
    body: str
