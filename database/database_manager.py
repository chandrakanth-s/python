from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.schema_declarative import Registrations, base, RegistrationStatus, OTP,\
    PasswordCredentials, DocumentUploadDetails, PostDetails, PostDocumentMapping,\
    PostComments, PostLikes
from utilities.utils import generateUniqueId, getOTP, getRandomId, isEmpty,\
    getServerDateTime, getNextStartDateTime
from utilities import messages, serializer
from datetime import datetime
from sqlalchemy import and_
 
# engine = create_engine('sqlite:///mstartup.sqlite')
engine = create_engine('mysql://root@localhost/startup')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

 
def isUserExists(mdn):
    session = DBSession()
    queryResult = session.query(Registrations).filter(Registrations.mdn == mdn).first()
    return queryResult
    
def createUser(name, mdn, channel):
    session = DBSession()
    resitrationStatus = ""
    actorId = generateUniqueId()
    userState = isUserExists(mdn)
    if(userState == None):
        newUser = Registrations(actor_id = actorId, name=name, mdn = mdn, channel = channel, status = RegistrationStatus.ACTIVATION_PENDING)
        session.add(newUser)
        session.commit()
        newOTP = OTP(actor_id = actorId, otp = getOTP())
        session.add(newOTP)
        session.commit()
        resitrationStatus = ""
    else:
        resitrationStatus = userState
    return resitrationStatus

def activateUser(mdn, otp):
    session = DBSession()
    activationStatus = ""
    userState = isUserExists(mdn)
    if(userState == None):
        activationStatus = messages.error_user_not_exits
    elif(userState.status == RegistrationStatus.ACTIVE):
        activationStatus = messages.error_user_already_activated
    else:
        queryResult = session.query(OTP).filter(and_(OTP.actor_id==userState.actor_id , OTP.otp==otp)).all()
        #, OTP.created_date.between(datetime.now(),datetime.now()-timedelta(minutes=1))
        if(len(queryResult) > 0):
            session.query(Registrations).filter(Registrations.actor_id==userState.actor_id).update({Registrations.status:RegistrationStatus.ACTIVE})
            session.commit()
        else:
            activationStatus = messages.error_otp_expired
    return activationStatus

def createPassword(actorId, authKey):
    session = DBSession()
    status = True
    if(not isPasswordCreated(actorId)):
        newPassword = PasswordCredentials(actor_id = actorId, password = authKey)
        session.add(newPassword)
        session.commit() 
    return status

def isPasswordCreated(actorId):
    session = DBSession()
    status = False
    queryResult = session.query(PasswordCredentials).filter(PasswordCredentials.actor_id==actorId).all()
    if(len(queryResult) > 0):
        status = True
    return status
    
def isValidPassword(actorId,authKey):
    session = DBSession()
    queryResult = session.query(PasswordCredentials).filter(PasswordCredentials.actor_id==actorId).first()
    status = (queryResult.password == authKey)
    return status    

def addDocument(documentPath,documentType):
    session = DBSession()
    documentId = getRandomId()
    newDocument = DocumentUploadDetails(document_id = documentId, document_path=documentPath, type = documentType)
    session.add(newDocument)
    session.commit()
    return documentId

def updateProfilePicture(documentId, mdn):
    session = DBSession()
    session.query(Registrations).filter(Registrations.mdn==mdn).update({Registrations.document_id : documentId , Registrations.created_date:datetime.now()})
    session.commit()
    status = True
    return status

def isUserExistsByActorId(actorId):
    session = DBSession()
    user = session.query(Registrations).filter(Registrations.actor_id==actorId).first()
    return user

def createPost(title,description,actorId,documents):
    session = DBSession()
    status = None
    user = isUserExistsByActorId(actorId)
    if(user == None):
        status = messages.error_user_not_exits
    elif (user.status!=RegistrationStatus.ACTIVE):
        status = messages.error_not_activated
    else:
        postId = getRandomId()
        newDocument = PostDetails(poster = actorId, post_id = postId, title = title, description = description)
        session.add(newDocument)
        session.commit()
        if(len(documents)>0): 
            documentsList = []
            for i in range(len(documents)):
                documentsList.append(PostDocumentMapping(post_id = postId, document_id = documents[i]))
            session.add_all(documentsList)    
            session.commit()
              
    return status

def getPosts(cutOffTime,actorId):
    if(isEmpty(cutOffTime)):
        cutOffTime = getServerDateTime()
    endDate = getNextStartDateTime(cutOffTime)
    session = DBSession()
    postsResult = session.query(PostDetails).filter(and_(PostDetails.created_date>cutOffTime , PostDetails.created_date<=endDate)).all()
    tempList =[]
    for postItem in postsResult:
        postItemDict = postItem.serialize()
        documentQueryResult = session.query(DocumentUploadDetails).filter(and_(DocumentUploadDetails.document_id==PostDocumentMapping.document_id, PostDocumentMapping.post_id==postItem.post_id)).all()
        postItemDict.update({"documents":serializer.Serializer.serialize_list(documentQueryResult)})
        postItemDict.update({"poster": isUserExistsByActorId(postItem.poster).serialize()})
        postItemDict.update({"comments": getCommentCount(postItem.post_id)})
        likes = getLikes(postItem.post_id)
        postItemDict.update({"likes": len(likes)})
        postItemDict.update({"isLiked": actorId in str(likes)})
        tempList.append(postItemDict)  
    return tempList

def getCommentCount(postId):
    session = DBSession()
    result = session.query(PostComments).filter(PostComments.post_id==postId).all()
    return len(result)

def getLikes(postId):
    session = DBSession()
    result = session.query(PostLikes.liked_by).filter(PostLikes.post_id==postId).all()
    return result

def deletePost(postId,actorId):
    session = DBSession()
    post = session.query(PostDetails).filter(PostDetails.post_id == postId).first()
    status = False
    print (post)
    if(post!=None):
        if(post.poster == actorId):
            session.query(PostDocumentMapping).filter(PostDocumentMapping.post_id==postId).delete()
            session.query(PostDetails).filter(PostDetails.post_id==postId).delete()
            session.commit()
            status = True
    return status

def addComment(postid, commenterId, comment):
    session = DBSession()
    status = None
    user = isUserExistsByActorId(commenterId)
    if(user == None):
        status = messages.error_user_not_exits
    elif (user.status!=RegistrationStatus.ACTIVE):
        status = messages.error_not_activated
    else:
        result = session.query(PostDetails).filter(PostDetails.post_id==postid).all()
        if(len(result)>0):
            newComment = PostComments(comment=comment,poster=commenterId, post_id = postid)
            session.add(newComment)
            session.commit()
        else:
            status = messages.error_adding_comment
    return status

def likePost(postid, likedBy):
    session = DBSession()
    status = None
    user = isUserExistsByActorId(likedBy)
    if(user == None):
        status = messages.error_user_not_exits
    elif (user.status!=RegistrationStatus.ACTIVE):
        status = messages.error_not_activated
    else:
        result = session.query(PostLikes).filter(and_(PostLikes.post_id==postid,PostLikes.liked_by==likedBy)).all()
        if(len(result)>0):
            session.query(PostLikes).filter(and_(PostLikes.post_id==postid,PostLikes.liked_by==likedBy)).delete()
            session.commit()
            status = None
        else:
            newLike = PostLikes(post_id=postid,liked_by=likedBy)
            session.add(newLike)
            session.commit()
            status = None
    return status

        