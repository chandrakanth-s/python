from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import enum
from datetime import datetime
from sqlalchemy import Enum, DateTime
from utilities.serializer import Serializer
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.dialects.mysql.types import TEXT
from utilities.utils import getServerDateTime
 
base = declarative_base()

class RegistrationStatus(str, enum.Enum):
    ACTIVE = 1
    INACTIVE = 2
    ACTIVATION_PENDING = 3
    
class FeedType(str, enum.Enum):
    GENERAL = 1
    MY_FEED = 2
    GROUP = 3
       
     
class Registrations(base, Serializer):
    __tablename__ = 'registrations'
    id = Column(Integer, primary_key=True)
    actor_id = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    mdn = Column(Integer, nullable=False)
    channel = Column(String(250), nullable=False)
    status = Column(Enum(RegistrationStatus))
    document_id = Column(String(250), nullable=True)
    created_date = Column(DateTime, default = datetime.now())
    modified_date = Column(DateTime, default = datetime.now())
    __table_args__ = (UniqueConstraint('actor_id',name='actor_id'),)
     
    def serialize(self):
        d = Serializer.serialize(self)
        
        if('createdDate' in d):
            del d['createdDate']
        
        if('modifiedDate' in d):
            del d['modifiedDate']
            
        return d
  
class PasswordCredentials(base):
    __tablename__ = 'password_credentials'
    id = Column(Integer, primary_key=True)
    actor_id = Column(String(250), ForeignKey('registrations.actor_id'))
    password = Column(String(250), nullable=False)
    created_date = Column(DateTime, default = datetime.now())
    modified_date = Column(DateTime, default = datetime.now())
    
class OTP(base):
    __tablename__ = 'otp'
    id = Column(Integer, primary_key=True)
    actor_id = Column(String(250), nullable=False)
    otp = Column(String(250), nullable=False)
    created_date = Column(DateTime, default = datetime.now())
    
class DocumentUploadDetails(base):
    __tablename__ = 'document_upload_details'
    id = Column(Integer, primary_key=True)
    document_id = Column(String(250), nullable=False)
    document_path = Column(String(250), nullable=False)
    type = Column(String(250), nullable=False)
    created_date = Column(DateTime, default = datetime.now())
    __table_args__ = (UniqueConstraint('document_id',name='document_id'),)
    
    def serialize(self):
        d = Serializer.serialize(self)
        if('createdDate' in d):
            del d['id']
        if('createdDate' in d):
            del d['createdDate']
        if('modifiedDate' in d):
            del d['modifiedDate']
        return d
    
class PostDetails(base):
    __tablename__ = 'post_details'
    id = Column(Integer, primary_key=True)
    poster = Column(String(250), ForeignKey('registrations.actor_id'))
    post_id = Column(String(250), nullable=False)
    title = Column(String(250), nullable=False)
    description = Column(TEXT, nullable=True)
    type = Column(Enum(FeedType), default = FeedType.GENERAL)
    created_date = Column(String(250), default = getServerDateTime())
    modified_date = Column(String(250), default = getServerDateTime())
    __table_args__ = (UniqueConstraint('post_id',name='post_id'),)
    documentsList =  [{"chandra":"Kanth"}]
    
    def serialize(self):
        d = Serializer.serialize(self)        
        if('modifiedDate' in d):
            del d['modifiedDate']
        return d
    
    def updateDocuments(self,documents):
        self.documentsList.append(documents)
    
class PostDocumentMapping(base):
    __tablename__ = 'post_document_mapping'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post_details.post_id'))
    document_id = Column(String(250), ForeignKey('document_upload_details.document_id'))
    created_date = Column(DateTime, default = datetime.now())
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
class PostComments(base):
    __tablename__ = 'post_comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post_details.post_id'))
    comment = Column(String(250), nullable=False)
    poster = Column(String(250), ForeignKey('registrations.actor_id'))
    created_date = Column(DateTime, default = datetime.now())
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
class PostLikes(base):
    __tablename__ = 'post_likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(String(250), ForeignKey('post_details.post_id'))
    liked_by = Column(String(250), ForeignKey('registrations.actor_id'))
    created_date = Column(DateTime, default = datetime.now())
    
    def serialize(self):
        d = Serializer.serialize(self)
        return d
    
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
#engine = create_engine('sqlite:///mstartup.sqlite')

engine = create_engine('mysql://root@localhost/startup')
engine.execute("CREATE DATABASE IF NOT EXISTS startup") #create db
engine.execute("USE startup")

# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
base.metadata.create_all(engine)
