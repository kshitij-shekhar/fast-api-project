from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
app=FastAPI()

#Fastapi will validate the post request based on the 
#Type fields provided here
my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},
          {"title":"title of post 2","content":"content of post 2","id":2}]

# def get_postid(id):
#     for post in my_posts:
#         if post['id']==id:
#             return post

class Post(BaseModel):#pydantic model for our API schema
    title : str
    content : str
    published : bool = True #if user/client doesn't provide published field data, there's a default
    #value for it
    rating : Optional[int] = None #optional field, if not provided by client, will default to None


@app.get("/")
def root():
    return {"message":"Hello World"}

@app.get("/posts")
def get_posts():
    return {"Data":my_posts}

@app.post("/posts")
def create_posts(msg_body : Post): #Body is a FastAPI object
    # retreives the body passed with the post request, converts it to a dictionary(data passed
    # as json) and stores it in the msg_body variable
    # print(msg_body)
    # return {"message":"successfully created posts"}
    # return {"new_post":f"title : {msg_body['title']} \
    #         contents : {msg_body['content']}"}
    # print("title : ",msg_body.title)
    # print("content : ",msg_body.content)
    # return {"data":"new post"}
    post_dict=msg_body.dict()
    post_dict['id']=randrange(0,1000000)#choose a large enough range for unique ID
    my_posts.append(post_dict)
    return {"data":post_dict}#return the newly created posts after storage

#Fastapi parses path operations top down
@app.get("/posts/latest")
def get_latest():
    return my_posts[-1]


#retreive a single post
@app.get("/posts/{id}")#id path param
def get_post(id:int):
    # id=int(id)
    for post in my_posts:
        if post["id"]==id:
            return {f"post with ID : {id}":post}