from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
app=FastAPI()

#Fastapi will validate the post request based on the 
#Type fields provided here

class Post(BaseModel):#pydantic model
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
    return {"Data":"Your posts"}

@app.post("/createposts")
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
    return {"data":msg_body.dict()}