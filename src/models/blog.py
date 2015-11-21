import uuid
import datetime

from src.database import Database
from src.models.post import Post

__author__ = 'ibininja'

class Blog:
    #Note here that you would have different blogs so each would have its own attributes
    #That is why it is a normal class with init method
    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id=uuid.uuid4().hex if id is None else id

    #This is a normal function, without parameters because by default you can't use this without initializing it. So that's is why you just use the self to access the parameters.
    def new_post(self):
        title = input("Enter Posts Tile: ")
        content = input("Enter content: ")
        date = input("Enter post date, or leave blank for today (in format DDMMYYYY): ")

        if date == "":
            date=datetime.datetime.utcnow()
        else:
            date = datetime.datetime.strptime(date,"%d%m%Y")
        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)
        post.save_to_mongo()


    #Note that this is classmethod. Reasons are we are retrieving posts so all would have the same approach. or the same method of retrieving posts.
    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return{
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    #The classmethod converts the returned values/data to an object of the current class or cls passed.
    #This approach is very usefull to make changes to the values and store to DB or even to use the methods.
    @classmethod
    def from_mongo(cls, id):
        blog_data=Database.find_one(collection='blogs', query={'id':id})
        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id']
                    )