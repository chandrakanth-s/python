from flask import Blueprint
from utilities import messages
from flask import request
from database import database_manager as manager
from data.BaseResponse import BaseResponse
from data.PostsResponse import PostsResponse
from flask.json import jsonify

post_api = Blueprint('post_api', __name__)

@post_api.route('/createPost', methods=['POST'])
def createPost():
    baseResponse = BaseResponse()
    title = request.json['title']
    description = request.json['description']
    actorId = request.json['actorId']
    documents = []
    if('documents' in request.json):
        documents = request.json['documents'] 
    baseResponse.status = False
    execState = manager.createPost(title, description, actorId, documents)
    if(execState==None):
        baseResponse.status = True
        baseResponse.message = messages.success_create_post
    else:
        baseResponse.message = execState
    
    return jsonify(baseResponse.serialize())


@post_api.route('/fetchPosts', methods=['GET'])
def fetchPosts():
    baseResponse = PostsResponse()
    baseResponse.status = True
    baseResponse.message = messages.success_post_fetch
    lastFetchDateTime = request.args.get('cutOffTime')
    actorId = request.args.get('actorId')
    baseResponse.posts = manager.getPosts(lastFetchDateTime,actorId)  
    return jsonify(baseResponse.serialize())

@post_api.route('/deletePost', methods=['DELETE'])
def deletePost():
    baseResponse = PostsResponse()
    baseResponse.message = messages.error_delete_post
    baseResponse.status = manager.deletePost(request.json['postId'], request.json['actorId'])
    if(baseResponse.status):
        baseResponse.status = True
        baseResponse.message = messages.success_post_delete
    return jsonify(baseResponse.serialize())

@post_api.route('/addComment', methods=['POST'])
def addComment():
    baseResponse = BaseResponse()
    comment = request.json['comment']
    postId = request.json['postId']
    commenterId = request.json['commenterId']
    status = manager.addComment(postId,commenterId,comment)
    if(status == None):
        baseResponse.status = True
        baseResponse.message =  messages.success_comment_added
    else:
        baseResponse.status = False
        baseResponse.message = status
    return jsonify(baseResponse.serialize())

@post_api.route('/likePost', methods=['POST'])
def likePost():
    baseResponse = BaseResponse()
    postId = request.json['postId']
    likedBy = request.json['likedBy']
    status = manager.likePost(postId,likedBy)
    if(status == None):
        baseResponse.status = True
        baseResponse.message =  messages.success_liked_update
    else:
        baseResponse.status = False
        baseResponse.message = status
    return jsonify(baseResponse.serialize())

